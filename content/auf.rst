Agence Universitaire de la Francophonie
#######################################

:date: 2009-09-01
:slug: auf
:authors: Olivier Larchevêque
:lang: fr
:summary: Développement des systèmes d'informations de l'AUF
:category: job

Système de Gestion des Ressources Humaines
------------------------------------------

Ce projet a été développé spécifiquement pour les besoins des ressources humaines de l'AUF. Il est composé de plusieurs modules:

* RH (personnels, contrats, rémunérations, détachement, devise...)
* DAE : demande d'autorisations d'embauches
* Recrutement : offre d'emplois, soumissions, sélection couplée au site institutionnel
* Rapports : masse salariale, tâches à prévoir...

Cet outil se base sur un mécanisme de permissions complexe, selon les régions et groupes du personnel mais aussi des workflows. Cet aspect fait l'objet de tests unitaires d'accès.

Le développement a été incrémental sous forme agile.

*** Django, buildout, git, workflow, permissions, historisation, RH, SAML ***


Évaluation du personnel
-----------------------

Outil Django pour gérer les campagnes d'évaluations au sein de l'AUF.

*** Django, buildout, git, SAML ***


Savoirs en partage
------------------

Ce projet est un portail des ressources scientifiques et pédagogiques de l'AUF. Il moissonne plusieurs sites pour centraliser ces informations.

Il offre un répertoire de chercheurs avec des fonctionnalités pour construire des communautés.

Ce site est construit en Django, avec le moteur de recherche Sphinx. Les moissonnages utilisent des formats d'échanges standard quand ils existent, comme  OAI.

[Savoirs en partage](http://www.savoirsenpartage.auf.org)

*** Django, buildout, Sphinx, OAI, communautés ***


Assistance informatique
-----------------------

Ce projet consiste à fournir un moyen aux employés de l'AUF pour rapporter leurs problèmes afin d'établir une base de connaissances. 
Il peuvent rapporter leurs problèmes par courriel ou directement sur le portail.
Cet outil est un fork de l'Application Jutda.

*** Django, assistance, tracker, courriels ***


Site institutionnel
-------------------

J'ai participé à la refonte du site [institutionnel](http://auf.org) de l'AUF. Ce portail se base sur **django-cms** avec plusieurs plugins pour se coupler à nos données de références et nos systèmes d'informations.

***Django, django-cms, support, maintenance ***


Portail informatique
--------------------

Ce projet est un CMS pour présenter l'information relative à l'administration des ressources informatique de l'AUF. Il a été construit avec **Django-cms**. Certains plugins ont été développés pour s'interfacer avec d'autres systèmes d'informations.

*** Django, Django-cms, SAML ***


Semaine tech
------------

J'ai donné des formations MVC, Django pour les techniciens de l'AUF.

[Programme](http://wiki.auf.org/wikiteki/Projet/SemaineTech/2011)

*** Django, cours, formation, MVC ***



Industrialisation et capitalisation
-----------------------------------

* Création de skeleton pour harmoniser les projets Django
* Statistiques centralisées de chaque application (Piwik)
* Rapports d'erreurs centralisés de chaque application  (Sentry)
* Création de modules Python réutilisées dans les applications (disponible dans un PyPI)

*** Django, Git, PyPI, modules, skeleton, Sentry, Piwik ***

Authentification centralisée
----------------------------


Développement et intégration d'un module Django, pour implanter l’authentification centralisée avec notre fournisseur d'identités en SAML.

*** Django, SAML, Logger ***
