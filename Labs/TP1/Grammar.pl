/*---------------------------------------------------------------*/
/* Telecom Paristech - J-L. Dessalles 2018                       */
/* Symbolic Natural Language Processing                 */
/*            http://teaching.dessalles.fr/SNLP                   */
/*---------------------------------------------------------------*/


% partial elementary English grammar

% --- Productions rules
s --> np(Number), vp(Number).

np(Number) --> det(Number), n(Number).
np(Number) --> det(Number), n(Number), pp.
np(number: singular) --> [kirk].

vp(Number) --> v([Number, opt]).
vp(Number) --> v([Number, opt]), np(_).
vp(Number) --> v([Number, one]), np(_).
vp(Number) --> v([Number, one]), pp.
vp(Number) --> v([Number, two]), np(_), pp.
vp(Number) --> v([Number, two]), pp, pp.

pp --> p, np(_).

% -- Lexicon
det --> [the].
det --> [my].
det --> [her].
det --> [his].
det --> [a].
det --> [some].
n --> [dog].
n --> [daughter].
n --> [son].
n --> [sister].
n --> [aunt].
n --> [neighbour].
n --> [cousin].
v --> [talks]; [grumbles]; [likes]; [gives]; [hates].
v --> [annoys]; [thinks]; [cries]; [barks]; [eats].
p --> [of]; [to]; [about].

% --- Our definitions
det(number: singular) --> [a].
det(number: plural) --> [many]; [some].
det(number: _) --> [the].
n(number: singular) --> [dog]; [sister]; [son].
n(number: plural) --> [dogs]; [sisters]; [sons].

v([number:singular, args:opt]) --> [eats].
v([number:plural, args:opt]) --> [eat].
v([number:singular, args:one]) --> [hates].
v([number:plural, args:one]) --> [hate].
v([number:singular, args:two]) --> [gives].
v([number:plural, args:two]) --> [give].
