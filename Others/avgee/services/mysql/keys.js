const RES_FORMAT = "render"; // json | render

if (process.env.NODE_ENV === "development") {
  const DBNAME = process.env.DEV_DBNAME;
  const HOST = process.env.DEV_HOST;
  const USER = process.env.DEV_USER;
  const PASSWORD = process.env.DEV_PASSWORD;
  const JWT_HTTPS = false;

  const PRIVATE_KEY = process.env.PROD_JWT_PRIVATE_KEY;
  const JWT_EXPIRY = process.env.PROD_JWT_EXPIRY;
  const SESSION_SECRET = process.env.PROD_SESSION_SECRET;
  const EMAIL_ADDRESS = process.env.PROD_EMAIL_ADDRESS;
  const EMAIL_PASSWORD = process.env.PROD_EMAIL_PASSWORD;
  const WEB_NAME = "http://localhost:8000/";

  module.exports = {
    DBNAME,
    HOST,
    USER,
    PASSWORD,
    PRIVATE_KEY,
    JWT_EXPIRY,
    JWT_HTTPS,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SESSION_SECRET,
    RES_FORMAT,
    WEB_NAME,
  };
}

if (process.env.NODE_ENV === "production") {
  const DBNAME = process.env.PROD_DBNAME;
  const HOST = process.env.PROD_HOST;
  const USER = process.env.PROD_USER;
  const PASSWORD = process.env.PROD_PASSWORD;
  const JWT_HTTPS = true;

  const PRIVATE_KEY = process.env.PROD_JWT_PRIVATE_KEY;
  const JWT_EXPIRY = process.env.PROD_JWT_EXPIRY;
  const SESSION_SECRET = process.env.PROD_SESSION_SECRET;
  const EMAIL_ADDRESS = process.env.PROD_EMAIL_ADDRESS;
  const EMAIL_PASSWORD = process.env.PROD_EMAIL_PASSWORD;
  const WEB_NAME = process.env.PROD_WEB_NAME;

  module.exports = {
    DBNAME,
    HOST,
    USER,
    PASSWORD,
    PRIVATE_KEY,
    JWT_EXPIRY,
    JWT_HTTPS,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    SESSION_SECRET,
    RES_FORMAT,
    WEB_NAME,
  };
}
