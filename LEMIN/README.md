<pre>
--------------------------------------------------------

   ._.      ._____.  .__.      .__.  ._.  .__.    ._.
   | |      | .___|  | . \    / . |  | |  |   \   | |
   | |      | |___.  | |\  \/  /| |  | |  | |\ \  | |
   | |      | .___|  | |  \__/  | |  | |  | | \ \ | |
   | |___.  | |___.  | |        | |  | |  | |  \ \| |
   |_____|  |_____|  |_|        |_|  |_|  |_|   \___|

--------------------------------------------------------

This project's purpose is to find, in a given graph, the shortest
way(s) to transport every lemin from start to end.
We admit that edges have all the same length and that we can not have
more than one lemin in each node at a time.
The program must find the most appropriate solution in less than 1s, 
even with 15 000 nodes and 15 000 lemins...

In this example : 

     [start]
      /  |
   [3]  [1]---[5]
   /     |     |
[4]-----[2]   [6]
         |    /
         [end]

If we have only one lemin to move from start to end, the shortest way is :
->	[start]-[1]-[2]-[end]
But! if we have more, at some point, depending on the number of lemins, 
it will be faster to use several differents pathes, such as :
->	[start]-[1]-[5]-[6]-[end]  &  [start]-[3]-[4]-[2]-[end]

Check out the school Subject.pdf file for more infos on the input/output.
This project has been done by abinois & ltimsit.

👌 enjoy :)
</pre>
