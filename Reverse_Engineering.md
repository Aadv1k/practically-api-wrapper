# Reverse Engineering practically.com


> **Note**
> These are some of the first requests sent when you load the login page

## `POST https://teach.practically.com/v1/teacherapp_v1/loginWithPassword`


### Request

**Body (Form)**

```json
Password: "password in md5",
Passwordsha256: "password in sha256",
LoginID: "login id",
```

> the `PHPSESSID` is the first indication of the site being a PHP-MVC 

### Response

Responds with the code `303`, being a redirect with the added cookies, which look like so:

- `ci_session=...;`
- `DisplayName=JOHN+DOE;` (the actual name)
- `SkipPhoneVerification=N;`
- `SkipEmailVerification=N;`
- `SkipVerification=N;`
- `UserType=Student;`
- `SurName=DOE;` (the actual surname)
- `idCountry=78;`

With an added location header, due to this being an redirect

- location:  `//teach.practically.com/v1/teacherapp_v1/home`

After this we are redirected to `/teach.practically.com/v1/teacherapp_v1/home` which redirects us back to this URL `https://teach.practically.com/webapp/dashboard.php?back=true&cookie={CI_SESSION}` which redirects us yet again to `teach.practically.com/webapp/dashboard.php?back=true` 

> I presume this is to set the session ID if it wasn't already, but it was so ??


## `GET /v1/studentweb/myschool/classes`

### Response

> I presume a `Student` can be enrolled in more than one `classes` with each having their own work

Returns HTML that contains an array of rows, which contain "class information", here is what that looks like

```html
<div class="row">
   <div class="col-xl-3 col-md-6 mb-4">
      <a href="//teach.practically.com/v1/studentweb/classdetail/CLASS_ID">
         <div class="card h-100">
            <div class="card-body">
               <div class="row align-items-center">
                  <div class="col mr-2">
                     <div class="font-weight-bold text-uppercase mb-1 text-gray-800">
                        CLASS_NAME					  
                     </div>
                     <div class="mb-0 text-gray-800">
                        CLASS_CORDINATOR_NAME
                     </div>
                  </div>
                  <div class="col-auto">
                     <button class="btn btn-success btn-xs">Enrolled</button>
                  </div>
               </div>
            </div>
         </div>
      </a>
   </div>
</div>
```


Where we have `CLASS_ID`, `CLASS_NAME` and `CLASS_CORDINATOR_NAME`


## `GET /v1/studentweb/classdetail/<CLASS_ID>/meetings`

Returns the first `100` meetings, complete or not.

### Response

> rather badly formatted might I add, output you see is prettified 

Returns HTML containing all the classes, completed or upcoming up-until now

```html
<div class="col-xl-4 col-md-6 mb-4">
   <div class="card h-100">
      <div class="card-body">
         <div class="row align-items-center">
            <div class="col mr-2">
               <div class="font-weight-bold text-uppercase mb-1 text-gray-800">
                  CLASS_TITLE
               </div>
               <div class="mb-0 text-gray-800">
                  <b>Start Time-:</b> 29 Dec 2023 01:35 PM						 IST (UTC +5:30)					  
               </div>
               <div class="mb-0 text-gray-800">
                  CLASS_TEACHER_NAME
               </div>
            </div>
            <div class="col-auto">
               <button class="btn btn-danger btn-xs">Completed</button>
            </div>
         </div>
      </div>
   </div>
</div>
```


## `POST /v1/studentweb/classdetail/<CLASS_ID>/meetings`

If you post instead, you can access more than the 100 meetings loaded

### Request

**Form**

```
offset	"100"
MeetingFilterType	"All"
isAjax	"1"
lmlistcount_count	"57"
```

### Response

This will return following `JSON`

```JSON
{
  "content": ""
  "dateFrom": null,
  "dateTo": null,
  "limitVal": 100,
  "isEndReached": "Y",
  "isAjax": "1",
  "MeetingList_count_all_1": 57,
  "MeetingList_count_ajax_1": 0,
  "lmlistcount_count": 57
}
```

The `content` is just additional HTML that loads 100 (or less) classes, along with some added JS event handlers. The caller of the above request appends this to the context 

## `GET /v1/studentweb/classdetail/<CLASS_ID>/assignments`

### Response

THis responds with HTML of card elements which looks like so

```html
<a 
  onclick="attachmentcompletion('_','MODULE_ID', 'MODULE_SECION_ID','', '','URL_TO_READ_PDF','Instructions','Completed')">
    <div class="card  main123_1058140" >							
        <div class="card-body" style="padding: 10px">
        <div class="row align-items-center" data-toggle="collapse" data-target="#collapseExample_">
            <div class="col mr-2">
                <div class="font-weight-bold text-uppercase mb-1 text-gray-800">
                <div style="display:none;" id="lmInstructions_1058140"></div>A

                <i class="fas fa-directions fa-2xl "></i>Instructions 

                <button class="btn  btn-xs"></button>
                </div>								  
            </div>

            </div>
        </div>
    </div>
</a>
```

Now let's try to figure this out, each "assignment" has two things, an instruction and a pdf, the `attachmentcompletion()` function, when cleaned up looks like this:

> Intrestingly, clicking on the element makes it "In-Complete" and clicking the PDF makes it "Complete"

```javascript
function attachmentCompletion(
  sectionNumber,                // 1
  idLearningModule,             // Learning Module
  idLearningModuleSection,      // Learning Module Section
  student, `                    // ??
  sessCourseInstanceId,         // ??
  url = '',                     // URL for the "view pdf"
  contentType,                  // Determine what "part" of the assignment we are clicking on, each being handled differently 
  sectionStatus                 // The current status
  ) {

    /* ... */

    var perComp = (contentType !== 'video' && contentType !== 'mpg') ? 100 : 0;
    $.ajax({
      url: '//teach.practically.com/v1/Studentweb/updateLearningSection/' + perComp,
      method: 'POST',
      data: {
        idCourseInstance: sessCourseInstanceId,
        idLearningModuleSection: idLearningModuleSection,
        idLearningModule: idLearningModule,
        SectionNumber: sectionNumber
      },
      async: false,
      success: function (result) {
        // if #lmInstructions_ is found, show a modal, else show some default message, such as "Please complete this"
        // change #lmStatusBtn to "In-Complete"
      },
  }
}
```



## `GET https://teach.practically.com/v1/files/shared/content/<ID[:2]>/<ID>/<ID>.pdf`

if the ID is `foobar`, the URL will look like this

```
https://teach.practically.com/v1/files/shared/content/fo/foobar/foobar.pdf
```

