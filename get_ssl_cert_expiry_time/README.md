# Get ssl certificate expiry time 

Simple python3 script to extract ssl certificate expiry date from url.

## Getting Started

This script was built to run under AWS Lambda with AWS API Gateway.

## Usage

With http get request with the query string: ?url=domain&port=443

https://4hajggzl94.execute-api.us-east-1.amazonaws.com/production?url=www.domain.com&port=443

Requirements
============

* AWS account
* AWS Api Gateway with Lambda proxy intergration.
* AWS Lambda
* Python 3.6

## Authors

* **Avi Keinan** - *Initial work* - [Avi Keinan](https://github.com/Burekasim)

## License

This project is licensed under the GPL3 License - see the [LICENSE.md](LICENSE.md) file for details

