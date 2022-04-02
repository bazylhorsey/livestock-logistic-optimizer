# Brooder Allocation Optimization

## Objective

A large turkey grower must transport young turkeys from barns called brooders to barns
called finishers. There are 10 brooders and 62 finishers within a ~50 mile radius of the
processing facility. Currently, the company transports birds from the brooder to the first
available (or one of a few available) finisher even if they must transport to the furthest finisher
from the brooder that is being emptied that week. Therefore, if a linear program (LP) could be
formulated seeking to minimize the distance traveled the company may benefit by reducing
transportation costs and bird mortality.

## Motivation

The company does not currently have a license for any of the more expensive linear
programming software that are capable of solving a problem so large (with 620 decision
variables). Before spending a lot of money on this type of software they have tasked an
employee with setting up a preliminary, scaled-down problem with some of the available free
software. This scaled-down version of the problem will consider only 4 brooders and 29 finishers
(116 decision variables).

## Problem Description

The objective function of the problem will be to minimize the miles driven between
brooders and finishers over one year
Before constraints can be written, a proper understanding of the turkey growing operation
must be acquired. The birds (called “poults” at this point in their life) are purchased and
delivered at one day old from nearby hatcheries and spend roughly the first 35 days of their lives
living in barns called brooders. A brooder can typically hold anywhere between 100,000 and
170,000 poults. After 35 days have elapsed and the poults have nearly outgrown the brooder barn
they are transported on trucks (approximately 3,000 at a time) to farms called finishers. A
finisher is comprised of two to five barns with each barn having a capacity of 11,000 birds. After
brooder barns are emptied they are cleaned and the bedding (of sawdust) is changed; this process
typically takes about 19 days. Once birds have been emptied into a finisher they grow for an
additional 105 days before being loading onto trucks and are taken to the plant. After a finisher is
emptied it is cleaned over a period of roughly 20 days and prepared for the next flock of birds.
Several years ago there was an international pandemic of avian flu which culled the birds
of many poultry operations in the region and around the world. Since that avian flu outbreak
poultry growers have enacted strict biosecurity measures to ensure the health and quality of their
birds. One such measure is to mandate that no birds of different age groups are mixed together.
For practical purposes, “same age” is taken to mean that they are born within one week apart.

There are a number of factors which might be relevant in the “real world” but cannot be
considered in this model due the difficulty involved in representing them mathematically. Some
of these factors include:

Bird mortality: typically mortality is roughly 3% in brooders and 12% in finishers. Bird
mortality could be described as stochastic and is dependent on travel time, weather, bird
stress, and overall bird health
Birds of the same age in different brooders: if birds of the same age are raised in different
brooders it is permissible for them to be placed at the same finisher

Inexactness of capacity: while brooders and finishers have certain capacities it is unusual
for them to contain that exact amount of birds. For example, sometimes a finisher barn
may be slightly overfilled with 11,500 birds or underfilled with only 10,000 birds.
Additionally, sometimes brooders will contain fewer than their capacity allows due to
mortality or the hatchery slightly underdelivering on an order

Inexactness of growing and cleaning times: often birds may stay in a brooder or finisher
for longer than 35 or 105 days. For example, if the processing facility is unable to keep
up with the production schedule (which was determine 1-2 years in advance) due to
insufficient labor, birds may end up staying in a finisher for an additional 30 days or
more. Additionally, a farmer may take shorter or longer than 19 or 20 days to clean their
barn after it is emptied
While important to consider, these points will not be factored into this particular model
formulation. However, should the company wish to run a full-scale model if this preliminary one
proves successful some of these may be wise to consider.

## Proposed Solution

A mixed-integer programming (MIP) formulation for the brooder allocation problem.

## Licensing

In order to run this Jupyter Notebook properly, you must have a valid Gurobi license. If you do not have one, you can request
an [evaluation license](https://www.gurobi.com/downloads/request-an-evaluation-license/?utm_source=Github&utm_medium=website_JupyterME&utm_campaign=CommercialDataScience)
as a _commercial user_, or download a [free license](https://www.gurobi.com/academia/academic-program-and-licenses/?utm_source=Github&utm_medium=website_JupyterME&utm_campaign=AcademicDataScience)
as an _academic user_.

<!-- ## HTML Example URL

https://gurobi.github.io/modeling-examples/facility_location/facility_location.html -->
