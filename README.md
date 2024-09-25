# MedBook Server

MedBook Server is a robust backend infrastructure for managing medical records, appointments, and patient data. Built with scalability and security in mind, this server provides a reliable foundation for the MedBook ecosystem.


## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)


## Features

- User authentication and authorization
- Patient data management (CRUD operations)
- Medical record management (CRUD operations)
- Appointment scheduling and management
- Search functionality for patients and medical records
- Secure data storage and encryption


## Technology Stack

- Node.js
- Express.js
- MongoDB
- Passport.js (authentication)
- JSON Web Tokens (JWT)


## Installation


### Prerequisites

- Node.js (>=14.17.0)
- MongoDB (>=4.4.0)
- npm (>=6.14.13)


### Steps
1. Clone the repository: 
   ```bash
git clone https://github.com/riteshp112/medbook-server.git```

2. Install dependencies:
   ```bash
        npm i```
3. Create a `.env` file with the following variables:
   ```makefile
PORT=3000
MONGO_URI=mongodb://localhost:27017/medbook
JWT_SECRET=your_secret_key```
4. Start the server:
  ```bash
      npm start```

## API Documentation


### Endpoints


- **POST /register**: Register a new user
- **POST /login**: Login an existing user
- **GET /patients**: Retrieve all patients
- **GET /patients/:id**: Retrieve a patient by ID
- **POST /patients**: Create a new patient
- **PUT /patients/:id**: Update a patient
- **DELETE /patients/:id**: Delete a patient
- **GET /appointments**: Retrieve all appointments
- **GET /appointments/:id**: Retrieve an appointment by ID
- **POST /appointments**: Create a new appointment
- **PUT /appointments/:id**: Update an appointment
- **DELETE /appointments/:id**: Delete an appointment


### API Request/Response Examples


Using tools like Postman or cURL, you can test API endpoints.


## Contributing


Contributions are welcome!


1. Fork the repository.
2. Create a feature branch.
3. Commit changes with descriptive messages.
4. Push changes to your fork.
5. Open a pull request.


## License


MedBook Server is licensed under the MIT License.


## Contact


For any questions, suggestions, or concerns, please open an issue or contact [Ritesh Patel](https://github.com/riteshp112).


