/*---------------------------------------------------------------*/
/* Telecom Paristech - J-L. Dessalles 2018                       */
/* Symbolic Natural Language Processing                 */
/*            http://teaching.dessalles.fr/SNLP                   */
/*---------------------------------------------------------------*/


% partial elementary English grammar

% --- Productions rules
s --> np(FS), vp([subj:FS,_]).
np(FS) --> det(FS), n(FS).
np(FS) --> det(FS), n(FS), pp.
vp(FS) --> v(FS).
vp(FS) --> v(FS), np(_).
vp(FS) --> v(FS), pp.
vp(FS) --> v(FS), np(_), pp.
vp(FS) --> v(FS), pp, pp.
pp --> p, np(_).

% -- Lexicon
det([number:_, person:3, sentience:_]) --> [the].
det([number:sing, person:3, sentience:_]) --> [a].
det([number:plur, person:3, sentience:_]) --> [some].
n([number:sing, person:3, sentience:true]) --> [dog].
n([number:sing, person:3, sentience:true]) --> [daughter].
n([number:plur, person:3, sentience:true]) --> [dogs].
n([number:plur, person:3, sentience:true]) --> [daughters].
n([number:sing, person:3, sentience:false]) --> [apple].
n([number:sing, person:3, sentience:false]) --> [door].
v([subj:[number:sing, person:3, sentience:true],event:false]) --> [grumbles].
v([subj:[number:sing, person:3, sentience:true],event:false]) --> [likes].
v([subj:[number:plur, person:3, sentience:true],event:true]) --> [eat].
v([subj:[number:plur, person:3, sentience:true],event:true]) --> [bark].
v([subj:[number:plur, person:3, sentience:false],event:false]) --> [charge].
v([subj:[number:sing, person:3, sentience:_],event:true]) --> [breaks].
v([subj:[number:sing, person:3, sentience:_],event:true]) --> [falls].
p --> [of].
p --> [to].
p --> [about].


