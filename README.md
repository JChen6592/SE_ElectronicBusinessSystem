# SE_ElectronicBusinessSystem
Team #8

By:
John Chen,
Praveena Shrestha,
Christian Castro,
Fayrouz Mikhael,

#### Prerequisites:
Have python 3 installed and Django 

#### Note:
The super user's login information is:

Username: P<br>
Password: Ppassword<br>

#### Project Statement:

The purpose of this software is to build a place where people can come to find and discover anything they might want to buy or sell online. Guess users only have the right to search and view products, while ordinary users have the right to view, sell, search and buy. 
The super user will have privileges that can affect GU and OU.

#### Project Specifications

SU: Superuser is created through Django by running python manage.py createsuperuser. After the superuser is created they have access to accept forms of GU to become an Ordinary user. They remove accounts, have access to ordinary users information, access to taboo words. 

Ordinary User: ordinary users are able to search, sell, and purchase items from other ordinary users. They can be removed by superuser if they violate guidelines.

Guess User: They must just submit a form to become gu but it doesn't have to be accepted by the superuser. They will just gain access to search for items. 

#### Required Electronic Business System Functionalities
[X] A GU can only browse/search available items based on title, keywords, price (fixed or a range
for bidding) and ratings.<br>

#### An OU can do the following tasks:
[X] 1. Have all the features of a GU.<br>
[X] 2. Submit to SUs the application to be an OU, which should include a unique id, the name, a
valid credit card number, address, phone number.<br>
[X] 3. Submit the bid to buy an available item.<br>
[X] 4. Submit to SUs the information (title, key words, price nature, at least one picture) of the
item(s) s/he wants to sell.<br>
[X] 5. Sell the item s/he posted; for fixed price, the first one who posted the purchase intention
should be chosen, otherwise the owner should provide a note justifying why the first one
is not chosen; for price range, the one with the second highest bids should be chosen,
otherwise the owner should provide a note of justification.<br>
[X] 6. Submit purchasing intentions if no such item exists in the system, once someone post
item(s) matching the keyword(s), the OU will receive notifications.<br>
[X] 7. File complaints to SUs against certain OUs whose item or payment has some problem or
explain to the SU about any complaint received from others.<br>
[ ] 8. Grade an OU after buying an item from him/her, 0 being the worst and 5 being the best.
An OU who has submitted too many low ratings, three 0 or 1 ratings in a row, or high
ratings, three 5 ratings in a row, will be warned by SU as possible reckless graders.<br>
[ ] 9. See his/her own transaction history.<br>
[X] 10. Change his/her password, name, address, phone and credit card number, but not the id.<br>
[ ] 11. An OU will become a VIP OU if her/his rating is &gt;= 4 (by at least 3 different OUs) or
spent more than $500 and without warnings, any VIP will receive 5% discount when
checking out. A VIP is moved to ordinary OU if his/her rating is below 4 automatically
or received one warning.<br>
[ ] 12. An OU can maintain a friend list who will receive discount and friend-only messages, the
OU is free to add/delete any OU from the list.<br>

#### An SU can perform the tasks below:
[X] 1. Process applications and decide who can be OU and who should be denied. The initial
password is the same as the id which the new OU is required to change the first time s/he
logs in.<br>
[X] 2. Process item information the OUs submitted intending to sell, some can be publicly
available on the platform and some may be denied with justifications. An OU whose item
is denied will be warned once.<br>
[X] 3. Process complaints: either removed or saved as justified ones after communicating with
the OU who was complained.<br>
[ ] 4. Send warnings to OUs who received two justified complaints or the average grade are
lower than 2 with at least 3 different evaluators, should an OU receive two warnings this
OU should be suspended from the system. A suspended OU will be notified when s/he
logs in and can choose to appeal or resign. The appeal can be either approved or denied
(then the user is removed).<br>
[X] 5. Have the right to remove any OU based on his/her judgment. A removed OU can log in
to the system for the last time to clear matters, then the account is deleted afterwards.<br>
[ ] 6. Collect transaction statistics for a certain period (a day or a week) or a certain OU.<br>
[X] 7. Maintain a taboo list with all inappropriate words, any OU’s keywords/name or items
containing taboo words will be replaced by *** and the OU received one warning and
required to change the word next time s/he logs in. [Don’t use real taboo words in your
list, use mock ones instead to not offend anyone]<br>

#### Other constraints:
[ ] 1. When logging in, the system should have personalized recommendations to the OU based
on his/her past search/purchase records, if no such information is available, the top 3
most popular items and OUs are displayed in the GUI.<br>
[ ] 2. OUs removed from the system by SUs will be blocked based on the name for future re-
application.<br>
[ ] 3. Items removed from the system by SUs will be blacklisted from system.<br>
[ ] 4. The tax of every sold item is automatically evaluated based on the address of the buying
OU (have a dictionary keeping the tax rate for different states).<br>
[X] 5. GUI is required but not necessarily web-based. (Our Project is web-based)<br>
[ ] 6. One creative feature worth 10% of the final project, such as speech interface,
shipping/delivery plans or image content-based search, if your feature if very creative,
your team will be rewarded by an up to 10% bonus.<br>

#### Implemented Functionalities that were later removed due to crashes and errors
[ ] Rating System<br>
[ ] Messaging System<br>
