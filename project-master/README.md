# Cooking for dummies

# Abstract
Eating is one of the core actions we do everyday. But cooking does not seem to be as core as eating, as precooked food seem to be more popular than ever. Moreover, with the restructuring of the society in terms of gender, cooking lessons are now meant for specialists that intend to work as cooks. Because of that, people don't necessarily know how to cook anymore.
Still, eating healthy and at a moderate price requires some cooking. How to combine the leftovers in your fridge? What are the most recommended spices to cook your Thanksgiving's turkey?
Our goal is to provide a very easy way to see which ingredients go along with which, and provide **simple food combinations** that are often used together, and to illustrate the **synergies between ingredients**.

## Project plan

### Dataset

We take our data from:
* Cooking recipes: infolab.stanford.edu/~west1/from-cookies-to-cooks/recipePages.zip 
* infolab.stanford.edu/~west1/from-cookies-to-cooks/recipeInfo.tar.gz

This data represents recipes gathered from several cooking websites. It contains recipes entries with info such as the calories (fat,proteins,carb) and the ingredients. Our main focus will be the ingredients list of each recipe, from which we intend to collect an exhaustive list of ingredients.

### Study of the database

As our main focus is the ingredients, we study the **words used in the recipes**. We look at the frequencies of words to better understand how we could clean the data from unwanted words such as 'teaspoon','cup',...

One idea is to plot the **sorted occurencies of words**, but also the **number of words with a given occurence** (for *i*, *f(i)* is the number of words that appear *i* times).

What we expect to observe is the well-known Zipf law (https://en.wikipedia.org/wiki/Zipf%27s_law), an empirical law stating that in a sufficiently large amount of textual data, the words tend to be used with proportions 1, 1/2, 1/3, ....

### Plans for the future

We would start by cleaning the data: as the study shows, we cannot easily cut off the words with the most occurencies: even if 'cup' is one of them, so is 'sugar'. One other idea is to manually remove the non-ingredients words.

Then we would create a database based on what we observe in the original database: Let *N* bet the total number of ingredients.
* There are N entries, one for each ingredient
* There is one column indicating the food type: we would like to avoid having salt appearing as a main synergy for half of the ingredients
* The N next columns would contain shared occurencies: for entry *i* and column *j*, the value corresponds to the number of recipes in which both *i* and *j* are used.

The next step is to create a basic website on which we could query the database: a query would be: *ingredient1*, and the output would be:
*ingredient1* has a strong synergy with *ingredient2*,*ingredient3*,...
In particular *ingredient1*,*ingredient2*,*ingredient5* is a great combination,
as well as *ingredient1*,*ingredient3*,*ingredient6*.
Another interesting option would be to query several ingredients.
Here are all the options we would like to implement:
* look only for 1 good accompanying food **/** look for synergies with multiple ingredients
* query for several ingredients
* specify what kind of accompanying food you are looking for (meat,fruit,spices,...)


## Question for TA

We did took note of your advice to modify and clarify our README. We hope it better corresponds to your expectations. If not, please do let us know what we still need to improve.


