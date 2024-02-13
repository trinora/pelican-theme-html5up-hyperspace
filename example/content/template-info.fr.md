Title: À propos de ce modèle
Slug: template-info
Date: 2024-02-12 00:00:00
Category: Pelican
Tags: Themes
Lang: fr
Summary: Il s'agit d'un portage vers Pelican du [modèle HTML5 UP Hyperspace](https://html5up.net/hyperspace) par [Trinora Software, Ltd.](https://trinora.software). Veulent en savoir plus? Lisez cet article !

Il s'agit d'un portage vers Pelican du [modèle HTML5 UP Hyperspace](https://html5up.net/hyperspace) par [Trinora Software, Ltd.](https://trinora.software). Sous licence Creative Commons Attribution 3.0. Veuillez conserver tous les avis d’attribution en place.

## Fonctionnalités du thème

### Sections de la page d'accueil
N'importe quelle page peut être ajoutée en tant que section à la page d'accueil. Ces sections apparaîtront sous les articles (si activées, voir `THEME_HOMEPAGE_INCL_ARTICLES`) et avant le pied de page. Ajoutez les métadonnées suivantes pour les pages applicables :

* HomePage_Sort : valeur numérique (en fait une chaîne, mais destinée à être numérique) donnant l'ordre de tri de la section sur la page. Cela ne prend effet que si plusieurs pages sont incluses en tant que section de page d'accueil.

* HomePage_Style : nom de classe pour le style CSS. Voir les règles `main.css` pour les classes `style ?`. Par exemple, `style1`, `style1-alt`, `style2`, etc.

### Tri des pages dans le menu de navigation
Ajoutez la clé `Menu_Sort` aux métadonnées de votre page pour contrôler l'ordre de tri de la page dans le menu de navigation. Cela ne prend effet que si `THEME_MENU_ONLY_MENUITEMS` est False et `DISPLAY_PAGES_ON_MENU` est True et que plus d'une page apparaît dans le menu.

### Image de l'article
Ajoutez la clé « Couverture » aux métadonnées de votre article avec un nom de fichier image comme valeur pour que cette image apparaisse dans les listes d'articles sous forme de vignette et d'image d'arrière-plan plein écran dans l'article lui-même.

## Paramètres spécifiques au thème
Voici les paramètres qui modifient le comportement de ce thème. Ces valeurs doivent être définies dans votre fichier `pelicanconf.py`.

### THEME_HIDE_ATTRIBUTION
*Booléen, False par défaut*

S'il est défini sur True, masquera l'avis d'attribution dans le pied de page. Veuillez vous assurer que vous répondez aux exigences de licence spécifiées dans le fichier README.md avant de définir cette valeur sur True !

### THEME_MENU_ONLY_MENUITEMS
*Booléen, False par défaut*

S'il est défini sur True, n'affichera que les liens dans le paramètre de configuration `MENUITEMS` dans le menu de navigation du site Web et ignorera les paramètres `DISPLAY_PAGES_ON_MENU` et `DISPLAY_CATEGORIES_ON_MENU`. S'il est défini sur False, le comportement du menu standard de Pelican sera utilisé.

### THEME_HOMEPAGE_INTRO_PAGE
*Slug de page, non défini par défaut*

S'il est défini sur un slug de page, le contenu de la page spécifiée sera rendu dans la section d'introduction de la page d'accueil, remplaçant l'intro par défaut. S’il n’est pas défini, défini sur une chaîne vide ou si le slug de page n’est pas trouvé, la section d’introduction par défaut sera utilisée. La section d'introduction par défaut affiche le nom du site, le sous-titre du site et un lien pour faire défiler la page d'accueil jusqu'à la section des articles.

### THEME_HOMEPAGE_INCL_ARTICLES
*Booléen, True par défaut*

S'il est défini sur True, les articles seront affichés sur la page d'accueil. Définissez sur False pour ne pas afficher les articles sur la page d'accueil.

### THEME_HOMEPAGE_ARTICLES_PAGINATION
*Chaîne, non définie par défaut*

Lorsque les articles sont affichés sur la page d'accueil (c'est-à-dire que `THEME_HOMEPAGE_INCL_ARTICLES` est défini sur True) et que la pagination est requise, si elle est définie sur "pagination", les contrôles de pagination seront affichés sur la page d'accueil. Toute autre chaîne sera interprétée comme la destination d'un lien « Afficher plus d'articles ». Si elle n’est pas définie, la pagination ne sera pas affichée sur la page d’accueil.

### THEME_FOOTER_PAGE
*Slug de page, non défini par défaut*

S'il est défini sur un slug de page, le contenu de la page spécifiée sera rendu dans le pied de page, remplaçant le pied de page par défaut. S’il n’est pas défini, s’il est défini sur une chaîne vide ou si le slug de page n’est pas trouvé, le pied de page par défaut sera utilisé. Le pied de page par défaut affiche les listes de liens « LIENS » et « SOCIAL ».

### THEME_LANG_*
**Chaîne de langue, diverses valeurs par défaut**

Pour prendre en charge la traduction du thème sans avoir besoin de plugins supplémentaires, il existe divers paramètres avec le préfixe « THEME_LANG_ » qui permettent de remplacer le texte anglais dans le thème. Cela inclut les titres et en-têtes de page, les étiquettes de boutons, etc. Vous pouvez inspecter les modèles de thème pour voir tous ces paramètres et comment ils sont utilisés. Certains paramètres prennent en charge les espaces réservés avec le filtre `format()` de Jinja.

## Suppression de l'attribution
La licence Creative Commons Attribution 3.0 exige que tous les avis d'attribution soient laissés en place. L'auteur original dispose d'une offre de licence commerciale qui permet de supprimer la mention d'attribution. Veuillez consulter [Pixelarity](https://pixelarity.com/) de l'auteur original et acheter un abonnement. Une fois qu'une licence commerciale a été achetée, l'attribution peut être supprimée avec le paramètre « THEME_HIDE_ATTRIBUTION » sur True.

## FAIRE

1. Ajouter la prise en charge des images et des biographies des auteurs ?
2. Besoin d'implémenter le modèle « period_archives.html ».
3. Styles CSS en ligne à nettoyer.
4. Quelques autres styles CSS laids à embellir.
5. Ajouter une fonctionnalité pour modifier la palette de couleurs du thème à partir des paramètres ?
6. Certaines pages de liste d'articles (au moins les balises, probablement d'autres) ont besoin d'une meilleure mise en page.

## Fichier Lisez-moi original (à partir de HTML5 UP)
> So I've had the wireframe for this particular design kicking around for some time, but with all
the other interesting (and in some cases, semi-secret) projects I've been working on it took me
a little while to get to actually designing and coding it. Fortunately, things have eased up
enough for me to finaly get around to it, so I'm happy to introduce Hyperspace: a fun, blocky,
one-page design with a lot of color, a bit of animation, and an additional "generic" page template
(because hey, even one-page sites usually need an interior page or two). Hope you dig it :)
>
>Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.
>
>(* = not included)
>
>AJ
>aj@lkn.io | @ajlkn

### Crédits

     Modèle HTML original :
        AJ (aj@lkn.io | @ajlkn)
        https://html5up.net/hyperspace

	Images de démonstration :
		Unsplash (unsplash.com)

	Icônes:
		Font Awesome (fontawesome.io)

	Autre:
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)
