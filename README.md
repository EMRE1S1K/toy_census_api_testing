Hi it's Emre! Hope everybody doing well and enjoyed the long weekend!:)
Let dive right in.
Set Up that I used {
    Python
    unittest
    request library
    json library
    Get and Post methods
}
I have tested here.
test_count_by_gender_with_top: This test case verifies the functionality
of counting genders with the specified "top" parameter.
It checks if the API returns the correct number of results based on the "top"
value and if the results are ordered from highest to lowest.

Bug ticket 1 P(N/A)= While I'm trying the retrieve gender count with top or nighter 
with GET and POST request server only provided me 3 gender counts.
(It should have get the all user gender counts.)

test_count_by_country: This test case checks the functionality of counting countries in the dataset.
It verifies that the API returns the correct count of countries and that
the results are ordered from highest to lowest.

Bug ticket 2 P(N/A)= While I'm trying to retrieve user country datas from
the server it has returned only value number that I provided on POST request
But it did not return any country names.

test_count_password_complexity: This test case tests the password complexity calculation.
It ensures that the API correctly determines the complexity value of passwords by counting the number of non-alphanumeric characters.
It also checks if the passwords are sorted in descending order of complexity.

Bug ticket 3 P(N/A) = While I'm trying to retrieve user password datas from the server
response code was 200 but data did not provide me any data about passwords.

In summary there is a lot of functionality need to be fixed and improved in the server side
in nature of these tasks that provided to me,I cannot really set any priority
at this time. 
And also I have tried to automate this tasks with python But I was not really successful.
I have been using frameworks such as(postman, cypress,robot) for a long time 
it was hard to hard coding but my eagerness to coding got another fire thanks to NewClassRoom.
I hope I would get a change to work and learn more about API Automation from professionals like you!

