""" 
Like the previous question, suppose we have a list of clicks and corresponding urls as follows:

url_counts = [
     "50,google.com",
     "60,yahoo.com",
     "10,yahoo.com",
     "1,wikipedia.org",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "2,wikipedia.org",
     "1,stackoverflow.com",
     "1,google.com"]

This time, we want to write a function that takes in this input as a parameter and returns a data structure containing the total number of clicks that were recorded on each url.

Note: Use of functions like "split", "index", "indexOf" are now permitted if desired.

Sample output:

url_clicks(counts) =>
google.com           51
yahoo.com:           370
wikipedia.org        3
sports.yahoo.com     40
stackoverflow.com    1

Complexity variables:
n: the number of strings in the list
(The length of the input string has a constant upper limit.)

"""

url_counts = [
    "50,google.com",
    "60,yahoo.com",
    "10,yahoo.com",
    "1,wikipedia.org",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "2,wikipedia.org",
    "1,stackoverflow.com",
    "1,google.com"
] 





def counter(url):
    count = ""
    for char in url:
        if char.isdigit():
            count += char
        if char == ',':
            break          
    return int(count)



def sum_clicks(counts):
    sum = 0
    for entry in counts:
        sum += counter(entry) 
    return sum
    

def counter2(counts):
    count  = {}
    for entry in counts:
        click_count, url = entry.split(',')
       
        if url in count:
            count[url] += int(click_count)
        else: 
            count[url] = int(click_count)
            
    return count



from collections import defaultdict
def counter3(counts):
    count  = defaultdict(int)
    for entry in counts:
        click_count, url = entry.split(',')
        count[url] += int(click_count)
            
    return count


print(counter3(url_counts))
