# Eternal Sovereign's DKP System

We use a zero-sum style DKP system with the ability to weight loot distribution by attendance.
This document aims to describe that system, how points enter the system and are distributed,
and how we specialize the system by being able to weight objects by attendance or caps.

Points come in to and leave the system soley through loot transactions.  Every awardable item
has a certain value.  When purchased, that value is awarded to all attendees that helped get
the item, divided evenly across all attendees.  Then, the value of that loot is deducted from
the person who won the item.

In this way, the system is entirely relationtional.  The balances are not some currency to be
spent, but a representation of the "stored worth" of your contributions versus your rewards.
Negative balances are not a bad thing, as the system is designed around 0.  Roughly half the
people in the system should have a negative value, or more accurately, half the points in the
system should be negative, such that when all points are added up, we get back to a total
"guild balance" of zero.

## Example loot points distribution

10 raiders go to a raid.  Two items drop, a dagger and a mask, both worth 100 DKP.  Rob buys
the dagger, and Mari buys the mask

Both items are bought.
```
100dkp for the dagger + 100dkp for the mask = 200 dkp total for the raid
200 total dkp raid worth / 10 raiders = 20 dkp per raider

All raiders get +20 DKP.

Rob bought the dagger, so he gets -100 DKP.
Mari bought the mask, so she gets -100 DKP as well.

Both Rob and Mari have a net DKP value of -80DKP for the raid
Each of the other raiders get +20DKP.

Lets check our zero-sum:

(-80 * 2) + (+20 * 8) = -160 + 160 = 0

We've maintained our zero sum integrity as well!
```

Loot is awarded to those who bid who have the highest DKP balance.

## Tier and the negative DKP cap

We use tier as a way to weight rare or critical item awarding to high attendance raider
to help the guild progress more quickly.  The tier values are arbitary, but we choose the
following values:

Tier A >= 60% raid attendance
Tier B >= 30% and < 60% raid attendance
Tier C < 30% raid attendance
Tier D < negative DKP cap, but any attendance

Tier D is unique in that it's not bassed off percentage, it's based off the current negative
DKP cap if one is set.  This allows us to deprioritize those who have received a lot of loot
without as much contribution to try to prevent "loot and scoot" candidates from joining the
guild, getting a lot of stuff, then leaving.

With Tier added to the system, loot is awarded to the highest DKP balance of the appropriate
tier.

### Examples

Take the following roster and values
```
Player     DKP     Attendance
------     ---     ----------
Rob        500     80% (A)
Mari       700     55% (B)
Bigslash   -700    100% (A/D)
Lilslash   300     12% (C)
Magikaid   200     60% (A)

Negative cap: -500
```

If a loot drops that's worth "100 A" that means it's perferenced to Tier A players and will
cost 100 DKP.  If Rob and Mari both bid on that item, Rob will win, as he is Tier A, despite
having a lower balance than Mari.

If an item that costs "100 B" is bid on, and Rob and Mari both bid, Mari would win as she has
the highest DKP balance.

If a "100 C" item is up for bid, and Lilslash and Magikaid both bid, Lilslash would win.

If a "100 A" item is up for bid, and  Bigslash and Lilslash both bid, Lilslash would win.  This
is because Bigslash is below the negative cap.  You can think of him as being temporarily Tier
D while he earns enough DKP to be above the negative cap.  If only Bigslash bid, he would still
get the item.
