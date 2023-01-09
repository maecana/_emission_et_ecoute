#### _EMISSION_ET_ECOUTE

> Auteur: Mae Anave Caña    
> Depuis: 2023-01-10    
> Updated: 2023-01-10    
> Version: 1.0    
> Github: [https://github.com/maecana/_emission_et_ecoute](https://github.com/maecana/_emission_et_ecoute)


##### Description: 
- Diffusion et écoute.
- Une application Django qui permet la diffusion de messages et l'écoute en temps réel.
- Cette application utilise des canaux et des websockets.


## Technologies

Listed below are the technologies used to make this app possible

| Name | Link | Description |
| ------ | ------ | ------ |
| Django | [https://docs.djangoproject.com/en/4.1/](https://docs.djangoproject.com/en/4.1/) | Backend Web Framework |


## Packages/Dependencies
- python3
- virtualenv
- Django


## Activate Virtual Environment
Create a virtual environment for the packages/dependencies
- Make sure python, and virtualenv is installed within the device 
- Go to the `VirtualEnvironments` folder, or create one if the folder does not exists: `cd '../VirtualEnvironments/`
- Create a virtual environment `python -m virtualenv _emmision_et_ecoute_venv`


## Activate Virtual Environment
Go to the `Virtual Environments` folder then activate the script:
- Go to `VirtualEnvironments` if you haven't created it already: `cd '../VirtualEnvironments/`
- Activate : `source _emmision_et_ecoute_venv/Scripts/activate`


## Run the Django
Start the django server. Go to the folder (usually root) where `manage.py` resides, then run.
- `cd /`
- `python manage.py runserver`
- Go to `http://127.0.0.1:8000/`


## Migration
- `python manage.py makemigrations`
- `python manage.py migrate`


## License: 
This code is licensed under the MIT License.
