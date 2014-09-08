Turbulent Média Inc
###################

:date: 2007-01-01
:slug: turbulent
:authors: Olivier Larchevêque
:lang: fr
:summary: Projets backend
:category: job

Framework de diffusion de contenus multimédia
---------------------------------------------


Le but de ce projet a été de construire un backend destiné à être utilisé par plusieurs frontends différents.

Le framework est construit selon un modèle MVC, et permet d'être manipuler à travers une interface générique d'administration en HTML ou via des API disponible pour un client Flash avec AMFPHP.

La diffusion des contenus fait intervenir beaucoup de règles métiers (contrats, annonceurs, espaces...) qui sont utilisées pour déterminer les rétributions de chaque annonceurs par rapport à l'utilisation de leurs contenus.

Ce framework a été utilisé pour produire le site de [http://toutpetits.telequebec.tv](http://toutpetits.telequebec.tv)

*** framework, PHP, AMFPHP,  MySQL, ORM,  webservices, HTML, CSS,  Javascript ***


Framework (centrifuge) pour portails Web
----------------------------------------

J'ai participé à l'améloration de notre **framework** maison en y
implantant un modèle **MVC**, et la gestion des relations dans l'**ORM**. 
1 an plus tard, tous les projets sont maintenant basé sur ce framework, et il est maintenant 
agrémenté de **memcache**.

Voici une liste des sites qui l'utilisent :

* http://etoiles.tv (terminé)
* [http://notrehistoire.canadiens.com](http://notrehistoire.canadiens.com)
* [http://urbania.ca](http://urbania.ca)
* [http://whoweare.ca](http://whoweare.ca)
* [http://www.cityspk.ca](http://www.cityspk.ca)
* http://deuxcestmieux.com (terminé campagne le lait)
* [http://destinationquebec.com](http://destinationquebec.com)

*** PHP, framework, drupal, wordpress, analyse, architecture, système, LAMP, linux, vim, apache, paypal, beanstream, optimal payment, memcached, smarty, AMFPHP ***


Audiogram
---------

Ce projet a été la reprise d'un existant en **PHP4**, à porter en **PHP5** et à finaliser pour sa mise en ligne.

J'ai développé une API (pour le frontend Flash) et une passerelle de paiement (**Optimal Payment**) dans le but d'acheter de la musique en ligne.

[https://boutique.audiogram.com](https://boutique.audiogram.com)

*** PHP4, PHP5, AMFPHP, Optimal payment ***


Dans ma bulle
-------------

J'ai implanté le module de paiement avec **beanstream** pour avoir la possibilité de faire des dons.

[http://www.dansmabulle.org](http://www.dansmabulle.org)

*** PHP, beanstream ***


BestHealthMag
-------------

Ce projet est la refonte et la migration d'un site sur la santé et la nutrition.
[http://www.besthealthmag.ca](http://www.besthealthmag.ca)

Il a été réalisé en **Drupal 6**. Le contenu a été repris d'un CMS propriétaire 
existant (sans documentation avec la base de données uniquement) et réinjecté avec un outil que j'ai développé.

Nous étions 2 pour le réaliser (un intégrateur + moi) :

* Apprentissage de Drupal (nouveau pour tous les 2, c'était une contrainte client)
* Spécifications techniques
* Migration de contenus (10000 environs)
* Migration du forum
* Réalisation en 2 mois

*** Drupal, migration, formation ***


CitySpeak
---------

Ce projet est l'initiative de la compagnie KungFuNumerik. Le site offre la possibilité de créer et d'envoyer des messages à partir de lettres extraites de photos.
[http://www.cityspk.ca](http://www.cityspk.ca)

Le backend est réalisé avec le framework interne, avec le moteur de template **smarty**. Pour dynamiser les interactions, c'est la librairie **jquery**  qui a été utilisé.

*** framework, PHP,  smarty, jquery ***
