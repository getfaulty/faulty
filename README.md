# faulty

A lightweight Sentry clone designed for simple error tracking.

![](https://raw.githubusercontent.com/getfaulty/faulty/main/faulty/static/images/screenshots/demo.png)

## Installation

While you can choose to use faulty directly, faulty is intended to work inside of a Docker container.

1. `docker pull ghcr.io/getfaulty/faulty`
2. `docker run -it -p 5000:5000 faulty`
3. Configure your application to use `http://public@localhost:5000/1` as its [`SENTRY_DSN`](https://docs.sentry.io/product/sentry-basics/dsn-explainer/)

The project ID section (`1`) can be replaced with any integer. The underlying project will be created with the first issue received for that project ID. 

## Credits

* Logo by [Tim Kim](https://www.instagram.com/timkimtimkim/)

## Similar Projects

* [Sentry](https://sentry.io/)
* [GlitchTip](https://glitchtip.com/)
* [Kent](https://github.com/willkg/kent)
