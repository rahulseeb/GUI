# GUI
A functioning graphical user interface used for adding card data into a video game called "The Outbound Ghost" .

How to use the graphical user interface. When you run the GUI on python a menu appears that allows you to enter different types of card data.
The buttons on the edges of the screen are the categories to enter the data, the 4 of them being data, start vars, moves or keywords.

Once you click one of the categories a dropdown menu appears which holds different subcategories. After you selected a subcategory an input
text box appears under the reset button which allows you to type in data. 

1) Firstly, enter some information into the text box then click submitwhen you are finished. In your console it will print out the
   dictionary holding the information you entered and the category you entered it into.
    For example if you clicked data -> instanceID and entered 1 as the instance id the dictionary would display :
    {'tooltips': [{'instanceID': '1'}], 'moves': [], 'keywords': {}}.

2) Then select your next category. When you do it should change the current category to the one you've selected as you can only
   enter information about one category at a time. Selecting categories in this order: data -> start vars -> moves -> keywords
   will ensure the category changes every time you select a new one. However moving backwards (let's say entering data from
   keywords then from moves). Once I select a subcategory in keywords, then enter information. After I swap to the moves category
   it will not reset the keywords subcategory so now you have 2 selected categories. If this happens you should click the
   'reset' button as it will reset all current categories to their starting value (data, start vars, moves or keywords).
   This would allow you continue entering information and select 1 category at a time.

3) If by chance you entered any incorrect information in the moves category or the data category click the remove button for
   options which allow you to remove the data you entered which is incorrect (starting at index 1). You can do so
   by typing m for moves or t for tooltips to reset the information. So if I entered 2 items from tooltips (the data category)
   I would enter t 2 to remove the 2nd value or t 1 to remove the first value. Other categories which are not moves or data
   will not have multiple instances of the same data. Keywords and start vars will only have instance of data per category,
   which can simply be changed by entering the information again to overwrite the current information stored in the dictionary.

5) If you are satisfied with your dictionary you created you can click the finish button which will then promt you to type in
   a name of the .json file you would create to store the dictionary in. Just type in the name (no .json at the end this is done
   automatically). Click the Finish button again after typing in the name and it will be created. The .json file will be created
   in the same directory as your python files by default.

6) If you are loading up a previously created .json file you would click the open button then proceed to type in the name of the file,
   then click the open button again. This loads your existing .json file so you can make changes and edit the .json file where you left
   off. If you want the file name to remain the same, simply click finish again and retype the same name as you did to open the file,
   it will overwrite your existing data with the new data.

Tip: When you submit data check the output of the python file as it prints your current dictionary with values. The reset button does this as well.
