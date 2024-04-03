**Project Overview**

The event management system is built on a modern tech stack to ensure scalability, maintainability, and performance.Django, a high-level Python web framework was best option, for its robustness and versatility in handling complex web applications. Django Rest Framework (DRF) was utilized to facilitate the creation of RESTful APIs, enabling seamless interaction with the frontend and other services.

**Tech Stack and Database Choice**

1. **Django**: Chosen for its extensive built-in features, including authentication, ORM, and admin interface, which expedited development and ensured code consistency.

2. **Django Rest Framework (DRF)**: Leveraged to build RESTful APIs, providing a structured and consistent approach to handling requests and responses.

3. **SQLite Database**: Selected for its simplicity and ease of integration with Django during development. While SQLite is ideal for prototyping and small-scale applications, it can be easily swapped out for more robust databases like PostgreSQL or MySQL for production deployment.

**Design Decisions and Challenges**

1. **API Design**:  RESTful design principles were used to create clear and intuitive endpoints for managing events. This design choice enhances interoperability and simplifies integration with frontend frameworks.

2. **Data Modeling**: Careful consideration was given to the data model design to ensure efficient storage and retrieval of event-related information. Relationships between models were established to maintain data integrity and facilitate complex queries.

3. **Error Handling**: Robust error handling mechanisms were implemented to provide informative error messages and gracefully handle unexpected scenarios, enhancing the overall user experience.


**Project Setup Instructions**

Follow these steps to set up and run the project:

1. **Clone the Repository**: 
   ```bash
   git clone <https://github.com/Biswojeet-Nayak/event_service/tree/main>
   ```

2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migration**: 
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server**: 
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**: 
   Open a web browser and navigate to `http://localhost:8000` to access the application.

**Prerequisites**

- Python 3.x installed on your system.
- Basic understanding of Django framework and RESTful API concepts.

By following these instructions, you'll have the event management system up and running, ready for further customization or deployment to production environments. 

# Event Service Project

This Django project, named `event_service`, facilitates the creation, listing, and finding of events through a RESTful API using Django Rest Framework.

**Usage:**

This project consists of the following apps:

1. **Data Creation App (`data_creation`):**
   - This app handles the creation and listing of events.
   - **URL patterns:**
     - `/event-management/create/`: Endpoint to create a new event (POST).
     - `/event-management/list/`: Endpoint to list all events (GET).
     - `/event-management/list/<int:id>/`: Endpoint to list event details by ID (GET).

2. **Event Finder App (`event_finder`):**
   - This app allows users to find events based on their location and a specified date.
   - **URL patterns:**
     - `/events/find/`: Endpoint to find events based on location and date (GET).

**Using Postman:**

1. **Create Event:**
   - **Endpoint:** `/event-management/create/` (POST)

2. **List Events:**
   - **Endpoint:** `/event-management/list/` (GET)

3. **Event Details:**
   - **Endpoint:** `/event-management/list/<int:id>/` (GET)

4. **Find Events:**
   - **Endpoint:** `/events/find/` (GET)

**Additional Information:**

- The `data_creation` and `event_finder` apps are already part of the `event_service` project.
- External APIs are utilized for weather information retrieval and distance calculation.
- All necessary settings and app configurations are already set up within the `event_service` project.


## Additional Information

**Data Creation App**

This Django app, named `data_creation`, facilitates the creation and listing of events through a RESTful API using Django Rest Framework.


**Usage:**

This app provides the following URL patterns:

- **Create Event:**  
  Endpoint: `/event-management/create/`  
  Method: `POST`  
  Description: Use this endpoint to create a new event.

- **List Events:**  
  Endpoint: `/event-management/list/`  
  Method: `GET`  
  Description: Use this endpoint to retrieve a list of all events.

- **Event Details:**  
  Endpoint: `/event-management/list/<int:id>/`  
  Method: `GET`  
  Description: Use this endpoint to retrieve details of a specific event identified by its ID.

**Using Postman:**

1. **Create Event:**
   - Open Postman and set the request type to `POST`.
   - Enter the URL `http://localhost:8000/event-management/create/`.
   - In the request body, provide the necessary data for creating a new event in JSON format.
   - Send the request.
   - You should receive a response with the details of the created event.

2. **List Events:**
   - Open Postman and set the request type to `GET`.
   - Enter the URL `http://localhost:8000/event-management/list/`.
   - Send the request.
   - You should receive a response with a list of all events.

3. **Event Details:**
   - Open Postman and set the request type to `GET`.
   - Enter the URL `http://localhost:8000/event-management/list/2/` (replace `2` with the ID of the event you want to retrieve details for).
   - Send the request.
   - You should receive a response with the details of the specified event.



**Event Finder App**

This Django app, named `event_finder`, allows users to find events based on their location and a specified date. It integrates with external APIs to provide weather information and calculate distances between the user's location and event locations.


**Usage:**

This app provides the following functionality:

- **Find Events:**  
  Endpoint: `/events/find/`  
  Method: `GET`  
  Description: Use this endpoint to find events based on the user's location and a specified date. The request should include parameters for latitude, longitude, and date. The response will include a paginated list of events within the next 14 days from the specified date, along with weather information and distance from the user's location to each event location.

**Using Postman:**

1. **Find Events:**
   - Open Postman and set the request type to `GET`.
   - Enter the URL `http://localhost:8000/events/find/`.
   - Include parameters for `latitude`, `longitude`, and `date` in the request.
   - Send the request.
   - You should receive a response with a paginated list of events, including weather information and distance from the specified location to each event location.

**Additional Information:**

- The `find_events` view in `views.py` handles the logic for finding events based on the user's location and specified date.
- External APIs are used to retrieve weather information (`get_weather`) and calculate distances (`calculate_distance`) between locations.
- The main project's URL configuration includes the `event_finder.urls` under the path `/events/`.

Feel free to explore and extend this app according to your project requirements!# event_service

