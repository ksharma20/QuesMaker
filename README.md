# QuesMaker
Django App to Create a Question Paper
It uses SQlite3 Database for Backend 

### How to run
- To run the project simply clone or download the zip file of the code
- then Extract it and goto that Extracted folder
- Now open Terminal in that Extracted Folder (Namely : quesMaker)
- Now run the command Onces you are in project dir (It must conatain a File name **manage.py**)
`python manage.py runserver`
- After that visit the url from your Browser `localhost:8000` or put this in your broswer

### Woohla Your Site is Up and Running
Consider Improving it, If you can

<br>

## Login Interface 
##### Credentials for superuser/ superadmin/ Developer

__Username - *admin*__

__password - *pass*__


##### Credentials for Normal Site user

__Username - *ksharma20*__

__password - *quesMaker*__

![image](https://user-images.githubusercontent.com/72795959/144738054-72c8115a-7215-4b9b-9d74-7f571ff4292b.png)

## Home Page
After Successfull login,Site Greets you with Your UserName (That is dissmissable)

![image](https://user-images.githubusercontent.com/72795959/144738079-c08984a8-4299-41ca-8145-6999992831af.png)


## Adding New Question Paper
Its Creates a New Entry in Database.

![image](https://user-images.githubusercontent.com/72795959/144738148-49836575-430c-4692-a89c-a37093e47ce8.png)


## Adding Questions to Question paper
After successfully creating a question paper you can add question to it right away

![image](https://user-images.githubusercontent.com/72795959/144738194-86d8c827-8892-4fae-b39b-7c05cff9eb0f.png)

I know this page is Not well structured, Because I used Django Forms in here Instead of HTML tags.
So, I will Structure it in later updates becuase it requires sometime.

## Next Question
After adding Information You can add next question.
It will Bring you to the same page But for Next Entry.
After Creating a Entry to Db for Pervious Question you Filled

![image](https://user-images.githubusercontent.com/72795959/144738521-6b0fe06a-6a3a-4bd7-9a69-908c9b3c47a7.png)

And You can Either keep on Adding Question or You can Go back to Home


## Edit Question Paper
If you See you can also Edit the Question Paper detail from Index / Home page 

![image](https://user-images.githubusercontent.com/72795959/144738583-f0cbd84c-fb9c-4261-a42e-a384a8d1f3cb.png)

as simple as it can be
Its Not much Different, But It Give you Power to update or Delete that Particular QuestionPaper

## Visit Question Paper
If you See you can also Visit the Question Paper detail from Index / Home page

*Ahhhhhh i just realised I have to Name it __view__ instead of __visit__ But we will do it later* 😒

##### *Updated* : Name Changed to **view** successfully 😎

![image](https://user-images.githubusercontent.com/72795959/144738822-4dda761c-5040-48fd-8a7a-0d4c38d85171.png)
![image](https://user-images.githubusercontent.com/72795959/144738832-3ca77614-3a61-4f2f-b0c9-6bb6277f7963.png)

Here we see all Questions inside that Question Paper.
We can Either Edit or Delete a Particular Question.
We can Also add New Questions to that Question Paper as Well.


## Flaws Left Intentionally
Haha😂 _I know I know_ __What you are thinking !!__ 😁. 
Yup I left something, Because I was daam to lazy to Change or Port them

#### Delete Request 
I used Get request to delete a Particular question as Well as Whole Question Paper. 
Therefore you know anyone can Delete it just by entering the Right URL Instead or a Delete Request.

I Could have Changed it into POST Request with csrf token But for That I had to create New forms and pages etc. 
So, that I can Send and Recieve a POST Request, Whereas as it is Now I have deleted Questions and Question papers 
Simply by using a <a> tag by sending them to that particular api link.
  
So Here you have it 
  The Flaw I left intentionally 🤷‍♀️🤷‍♂️
  
#### And Feel Free to Imporve it 
  Its always appericiated
