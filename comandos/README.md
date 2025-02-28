# Iniciar o projeto Django

    ```
    python -m venv venv
    . venv/bin/activate
    pip install django
    django-admin startproject project .
    python manage.py startapp contact
    ```

## Configurar o git

    ```
    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main
    # Configure o .gitignore
    git init
    git add .
    git commit -m 'Mensagem'
    git remote add origin URL_DO_GIT
    ```

## Migrando a base de dados do Django

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Criando e modificando a senha de um super usuário Django

    ```
    python manage.py createsuperuser
    python manage.py changepassword USERNAME
    ```

## Trabalhando com o model do Django

    ```
    # Importe o módulo
    from contact.models import Contact
    # Cria um contato (Lazy)
    # Retorna o contato
    contact = Contact(**fields)
    contact.save()
    # Cria um contato (Não lazy)
    # Retorna o contato
    contact = Contact.objects.create(**fields)
    # Seleciona um contato com id 10
    # Retorna o contato
    contact = Contact.objects.get(pk=10)
    # Edita um contato
    # Retorna o contato
    contact.field_name1 = 'Novo valor 1'
    contact.field_name2 = 'Novo valor 2'
    contact.save()
    # Apaga um contato
    # Depende da base de dados, geralmente retorna o número
    # de valores manipulados na base de dados
    contact.delete()
    # Seleciona todos os contatos ordenando por id DESC
    # Retorna QuerySet[]
    contacts = Contact.objects.all().order_by('-id')
    # Seleciona contatos usando filtros
    # Retorna QuerySet[]
    contacts = Contact.objects.filter(**filters).order_by('-id')

    >>> from contact.models import Contact
    >>> Contact
    <class 'contact.models.Contact'>
    >>> c = Contact(first_name='Gustavo')
    >>> c
    <Contact: Gustavo >
    >>> c.save()
    >>> c.save()
    >>> c.phone = '89666536598'
    >>> c.save()
    >>> c.delete()
    (1, {'contact.Contact': 1})
    >>> c
    <Contact: Gustavo Moreira>
    >>> c.first_name
    'Gustavo'
    >>> c.save()
    >>> c = Contact.objects.get(id=4)
    >>> c
    <Contact: Gustavo Moreira>
    >>> c.first_name = 'Helena'
    >>> c.save()
    >>> c
    <Contact: Helena Moreira>
    >>> c.pk
    4
    >>> c = Contact.objects.all()
    >>> c
    <QuerySet [<Contact: Joao miranda>, <Contact: luis miranda>, <Contact: Helena Moreira>]>      
    >>> for contato in c: contato.first_name       
    ...
    'Joao'
    'luis'
    'Helena'
    >>> c = Contact.objects.filter(id=1)
    >>> c
    <QuerySet [<Contact: Joao miranda>]>
    >>> c = Contact.objects.filter(id=4)
    >>> c
    <QuerySet [<Contact: Helena Moreira>]>
    ```
