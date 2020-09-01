# HelpTalent

HelpTalent is a platform where people who are willing to help, could provide resources to verified talented youths to pursue their dreams. This app is created using React and Django Framework.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/76a305404be9496f802d4f180e741966)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-139-Group-A-Frontend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/Team-139-Group-A-Frontend&utm_campaign=Badge_Grade_Dashboard)

## Intallation

1. clone this project `git clone https://github.com/BuildForSDGCohort2/helptalent`

1. navigate to the project dir `cd helptalent`

1. create and activate your python virtual environment

    on linux:
        ```python3 -m virtualenv env && source env/bin/activate```

    on windows:
        ```virtualenv env && env\Scripts\activate```

1. install the requirements `pip3 install -r requirements.txt`

1. rename `.env.example` file to `.env` and team members can request for the appropriate data to be inserted there from the admin. others can go ahead a put their data there.

## To run this project locally

1. make migrations

    on linux:
        ```python3 manage.py makemigrations```

    on windows:
        ```py manage.py makemigrations```

1. migrate to the database

    on linux:
        ```python3 manage.py migrate```

    on windows:
        ```py manage.py migrate```

1. create superuser and follow the prompts

    on linux:
        ```python3 manage.py createsuperuser```

    on windows:
        ```py manage.py createsuperuser```

1. start the development server

    on linux:
        ```python3 manage.py runserver```

    on windows:
        ```py manage.py runserver```

## For the Frontend

NB: make sure you have latest version of nodejs/npm, yarn installed.

1. run `npm install` so you can have the `node_modules`

1. If you want to edit our frontend, navigate to `public` and `src` and do your magic. Once your are done, you can run `yarn build` for it to reflect on your django live-server.
