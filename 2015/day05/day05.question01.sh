egrep '(.*[aeiou]){3}' input | egrep '(.)\1' | egrep -v 'ab|cd|pq|xy' | wc -l
