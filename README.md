# WWE Drafter

Following can be configured from the website
- Championships
- Matches
- Tag Teams
- Wrestler Profiles

The project was made to create **online templates.wwe drafts** based on some algorithm

### Current Champions (Original)
| Championship           | Champion                    |
|------------------------|-----------------------------|
| WWE Universal          | Roman Reigns                |
| WWE                    | Roman Reigns                |
| WWE Intercontinental   | Gunther                     |
| WWE United States      | Austin Theory               |
| WWE Raw Women's        | Bianca Belair               |
| WWE Smackdown Women's  | Rhea Ripley                 |
| WWE Raw Tag Team       | Kevin Owens/Sami Zayn       |
| WWE Smackdown Tag Team | Kevin Owens/Sami Zayn       |
| WWE Women's Tag Team   | Liv Morgan/Raquel Rodriguez |
| NXT                    | Carmelo Hayes               |
| NXT North American     | Wes Lee                     |
| NXT Tag Team           | Mark Coffey/Wolfgang        |
| NXT Women's            | Indi Hartwell               |
| NXT Women's Tag Team   | Alba Fyre/Isla Dawn         |


### Important commands
```shell script
# django-admin startproject Drafter

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py startapp wwe
```
