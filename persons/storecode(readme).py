#This file was made as a place to hold the code that Mason wrote for the list of dictionaries to display the table if we 
#want to go back and display the table this way, but when trying to use CSS to make it look nicer I found it easier to display the table 
#from getting the html from the converter that prof anderson provided us and then inputting that code straight into the index file and editing its appearence that way using CSS
#however, I didn't want to just delete what mason wrote so I made this file to store it just in case
#-ben

#the following is what we would put into the views file in this app
lstData = [
                {
                    "date_missing": "10/30/2009",
                    "last_name": "Sharmarice",
                    "first_name": "Halima",
                    "age_at_missing": "14",
                    "city": "Granger",
                    "state": "UT",
                    "gender": "F",
                    "race": "W"
                },

                {
                    "date_missing": "10/16/2015",
                    "last_name": "Martinez",
                    "first_name": "Kimberly",
                    "age_at_missing": "16",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "F",
                    "race": "M"
                },

                {
                    "date_missing": "07/23/2004",
                    "last_name": "Gomez",
                    "first_name": "Brenda",
                    "age_at_missing": "3",
                    "city": "Logan",
                    "state": "UT",
                    "gender": "F",
                    "race": "H"
                },

                {
                    "date_missing": "05/25/2003",
                    "last_name": "Bishop",
                    "first_name": "Acacia",
                    "age_at_missing": "1",
                    "city": "Salt Lake City",
                    "state": "UT",
                    "gender": "F",
                    "race": "W"
                },

                {
                    "date_missing": "08/03/2020",
                    "last_name": "Salazar",
                    "first_name": "Maria",
                    "age_at_missing": "14",
                    "city": "Snowville",
                    "state": "UT",
                    "gender": "F",
                    "race": "H"
                },

                {
                    "date_missing": "04/09/2020",
                    "last_name": "Hernandez-Soto",
                    "first_name": "Peggy",
                    "age_at_missing": "6",
                    "city": "Ogden",
                    "state": "UT",
                    "gender": "F",
                    "race": "H"
                },

                {
                    "date_missing": "06/24/2021",
                    "last_name": "Jimenez",
                    "first_name": "Lucero",
                    "age_at_missing": "14",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "F",
                    "race": "H"
                },

                {
                    "date_missing": "11/08/2013",
                    "last_name": "Colindres-Avila",
                    "first_name": "Yuris",
                    "age_at_missing": "17",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "F",
                    "race": "M"
                },

                {
                    "date_missing": "07/15/2021",
                    "last_name": "Harris",
                    "first_name": "Kandis",
                    "age_at_missing": "16",
                    "city": "Salt Lake City",
                    "state": "UT",
                    "gender": "F",
                    "race": "W"
                },

                {
                    "date_missing": "07/30/2006",
                    "last_name": "Seal",
                    "first_name": "Jaydan",
                    "age_at_missing": "1",
                    "city": "Garleys Wash",
                    "state": "UT",
                    "gender": "M",
                    "race": "W"
                },

                {
                    "date_missing": "06/13/2018",
                    "last_name": "Lizarraga",
                    "first_name": "Jose",
                    "age_at_missing": "13",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "M",
                    "race": "H"
                },

                {
                    "date_missing": "04/23/2020",
                    "last_name": "Cortez Trujillo",
                    "first_name": "Eztli",
                    "age_at_missing": "21",
                    "city": "North Ogden",
                    "state": "UT",
                    "gender": "M",
                    "race": "H"
                },

                {
                    "date_missing": "10/25/2017",
                    "last_name": "Fowles",
                    "first_name": "Juan",
                    "age_at_missing": "15",
                    "city": "Lehi",
                    "state": "UT",
                    "gender": "M",
                    "race": "M"
                },

                {
                    "date_missing": "08/20/2012",
                    "last_name": "Garcia",
                    "first_name": "Isai",
                    "age_at_missing": "17",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "M",
                    "race": "M"
                },

                {
                    "date_missing": "09/01/2015",
                    "last_name": "Smith",
                    "first_name": "Macin",
                    "age_at_missing": "17",
                    "city": "St. George",
                    "state": "UT",
                    "gender": "M",
                    "race": "W"
                },

                {
                    "date_missing": "01/26/2006",
                    "last_name": "Sisco-Ramirez",
                    "first_name": "Jose",
                    "age_at_missing": "4",
                    "city": "West Valley City",
                    "state": "UT",
                    "gender": "M",
                    "race": "M"
                }
            ] 

#I've commented the next part out to get rid of the errors but this is what we would put as the view function for the index page if we used the list above

#    context = {
    
#        "data" : lstData
#    }
#   return render(request, 'persons/index.html', context)



#in the index file we would then put this code if we wanted to display the table this way
#<head>
#        <title>Missing Persons</title>
#    </head>
#    <body>
        
#        <h4>Missing Persons Include:</h4>
#        <table style="border: 1px solid black;">
#              <tr>
#                  <th style="text-align: center; border: 1px solid black;">Date Missing</th>
#                  <th sstyle="text-align: center; border: 1px solid black;">Last Name</th>
#                  <th style="text-align: center; border: 1px solid black;">First Name</th>
#                  <th style="text-align: center; border: 1px solid black;">Age at Missing</th>
#                  <th style="text-align: center; border: 1px solid black;">City</th>
#                  <th style="text-align: center; border: 1px solid black;">State</th>
#                  <th style="text-align: center; border: 1px solid black;">Gender</th>
#                  <th style="text-align: center; border: 1px solid black;">Race</th>
#              </tr>            
#              {% for oPerson in data %}
#              <tr>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.date_missing }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.last_name }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.first_name }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.age_at_missing }}</td>  
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.city }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.state }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.gender }}</td>
#                  <td style="text-align: center; border: 1px solid black;">{{ oPerson.race }}</td>                                              
#              </tr>
#              {% endfor %}    
#          </table>
#      </body>




#this next code came with bootstrap and we can input it at the bottom of the index or any page to add a but more info
#<section class="page-section cta">
#            <div class="container">
#                <div class="row">
#                    <div class="col-xl-9 mx-auto">
#                        <div class="cta-inner bg-faded text-center rounded">
#                            <h2 class="section-heading mb-4">
#                                <span class="section-heading-upper">Our Promise</span>
#                                <span class="section-heading-lower">To You</span>
#                            </h2>
#                            <p class="mb-0">When you walk into our shop to start your day, we are dedicated to providing you with friendly service, a welcoming atmosphere, and above all else, excellent products made with the highest quality ingredients. If you are not satisfied, please let us know and we will do whatever we can to make things right!</p>
#                        </div>
#                    </div>
#                </div>
#            </div>
#        </section>