# Verifier

This tool is used to verify that surveys in this repo match the surveys on our survey hosting platform to prevent drift between the two.

## Usage

```
USAGE:
    verifier --password <password> --survey-name <survey-name> --username <username>

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information

OPTIONS:
    -p, --password <password>          
    -s, --survey-name <survey-name>    
    -u, --username <username>  
```

The username and password are the names provided by the SurveyHero [developer API console](https://www.surveyhero.com/user/account/api) after creating an API key.