# ASR MODEL DEPLOYMENT

## Server site

`cd flask_server`

1. Create *.flaskenv* file:

    Add the following configurations:

        FLASK_APP=<name of the running file>

        FLASK_ENV=<flask enviroment>

        FLASK_RUN_HOST=<server host>

        FLASK_RUN_PORT=<running port>

2. Install essential package:
  
    `pip install -r requirements.txt`

3. Run the server site with the *.flaskenv* configuration:

    `flask run`

## Client site

`cd client`

1. Create enviroment configurations:

    Create an `.env.development` file for development, `.env.production` file for production:

    Add these two following variables:

        REACT_APP_CHOST=<the server host>

        REATC_APP_CPORT=<the server running port>
        
        REACT_APP_ENV=<"dev" for development and "prod" for production>

2. Install all the needed packages:

   `npm install`

3. Start the client site:

    In development enviroment: `npm start`.

    In production enviroment: `npm build`.
