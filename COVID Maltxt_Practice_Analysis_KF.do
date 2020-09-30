/*****************************************************************************************/
/** Program: Practice_analysis															**/
/** Created by: Kriszta Farkas															**/
/** Date created: 09/29/2020															**/
/** Purpose: Practice analysis to explore standard DiD and conditional DiD approaches	**/
/**			 using outside dataset provided by Corinne									**/
/*****************************************************************************************/

/* read in data */
use "/Users/krisztafarkas/Desktop/Grad School/UCBerkeley/Ahern Research/GSR/COVID_Maltreatment and Domestic Violence/Analysis/Practice Analysis/epib672_dd.dta", clear

/* run standard vs. conditional approaches */
/* note: for simplicity, only looking at strong bans (primary enforcement) and 
		 not including confounders or population weights */
		 
/* 1. linear regression using standard approach:
   fixed effects on state (group) and month (time); 
   indicator variable for strong ban indexed by state-month (i.e., time-varying txt indicator);
   take into account clustering at the state level for correct statistical inference */
regress laccsvso strongban i.state i.time, cluster(state)

/* output full results table to word doc */
outreg2 using myreg_fulltables.doc, stats(coef ci) replace ctitle(Standard Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg.doc, stats(coef ci) keep(strongban) addtext(State FE, YES, Month FE, YES) replace ctitle(Standard Model)


/* 2. linear regression using conditional, within state approach */
xtreg laccsvso strongban i.time, fe i(state) vce(robust)

/* output full results table to word doc */
outreg2 using myreg_fulltables.doc, stats(coef ci) append ctitle(Conditional FE Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg.doc, stats(coef ci) keep(strongban) addtext(State FE, Conditional, Month FE, YES) append ctitle(Conditional FE Model)



/** create a months after variable to include lag exposure dummies to examine changes in effects over time **/
/* first, sort by state and time */
sort state time

/* create counter variable for months after text ban:
   =1 first month of text ban, =2 second month of text ban, etc. */
bysort state strongban: gen mosafter = _n if (strongban==1)
replace mosafter=0 if mosafter==.

/* examine distribution of mosafter variable */
tab mosafter

/** create years after variable - monthly estimates very imprecise **/
recode mosafter (0 = 0) (1/12 = 1) (13/24 = 2) (25/max = 3), gen(yrsafter)
tabulate mosafter yrsafter

/* run standard vs. conditional approaches */
/* 1. linear regression using standard approach:
   fixed effects on state (group) and month (time); 
   indicator variables for strong ban indexed by state-month (i.e., time-varying txt indicator);
   take into account clustering at the state level for correct statistical inference */
regress laccsvso i.yrsafter i.state i.time, cluster(state)

/* output full results table to word doc */
outreg2 using myreg2_fulltables.doc, stats(coef ci) replace ctitle(Standard Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg2.doc, stats(coef ci) keep(i.yrsafter) addtext(State FE, YES, Month FE, YES) replace ctitle(Standard Model)


/* 2. linear regression using conditional, within state approach */
xtreg laccsvso i.yrsafter i.time, fe i(state) vce(robust)

/* output full results table to word doc */
outreg2 using myreg2_fulltables.doc, stats(coef ci) append ctitle(Conditional FE Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg2.doc, stats(coef ci) keep(i.yrsafter) addtext(State FE, Conditional, Month FE, YES) append ctitle(Conditional FE Model)


/** create 6-month windows after variable - monthly estimates very imprecise **/
recode mosafter (0 = 0) (1/6 = 1) (7/12 = 2) (13/18 = 3) (19/24 = 4) (25/30 = 5) (31/max = 6), gen(halfyrsafter)
tabulate mosafter halfyrsafter

/* run standard vs. conditional approaches */
/* 1. linear regression using standard approach:
   fixed effects on state (group) and month (time); 
   indicator variables for strong ban indexed by state-month (i.e., time-varying txt indicator);
   take into account clustering at the state level for correct statistical inference */
regress laccsvso i.halfyrsafter i.state i.time, cluster(state)

/* output full results table to word doc */
outreg2 using myreg3_fulltables.doc, stats(coef ci) replace ctitle(Standard Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg3.doc, stats(coef ci) keep(i.halfyrsafter) addtext(State FE, YES, Month FE, YES) replace ctitle(Standard Model)


/* 2. linear regression using conditional, within state approach */
xtreg laccsvso i.halfyrsafter i.time, fe i(state) vce(robust)

/* output full results table to word doc */
outreg2 using myreg3_fulltables.doc, stats(coef ci) append ctitle(Conditional FE Model)

/* output only relevant coefficients to word doc */
outreg2 using myreg3.doc, stats(coef ci) keep(i.halfyrsafter) addtext(State FE, Conditional, Month FE, YES) append ctitle(Conditional FE Model)


