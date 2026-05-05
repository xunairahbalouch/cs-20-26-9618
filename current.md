In the context of A-Level 9618, we use Current (or CurrentPointer) so much
because it acts as the "Address" of the node we are currently holding in our
hand.

T In a Linked List, you cannot say "Go to index 5." You have
to start at the front and walk through the nodes one by one. Current is your
"finger" pointing at the specific box you are looking at right now.

Here are the four specific reasons we use it:

1. To "Walk" through the list (Traversal)

Since nodes are scattered in the array, the only way to find the next node is to
look at the nextnode value of the current one. Current =
linkedlist[Current].nextnode This is like saying: "Check the address written on
this node, and move my finger to that address."

2. To Check the Data

We need Current as an index to see what is inside the node. if
linkedlist[Current].data == ValueToDelete Without Current, the computer doesn't
know which index in the array to check.

3. To find the "Next Link"

When you delete a node, you need to "hop" over it. To do that, you need to know
what the deleted node was pointing to. linkedlist[Previous].nextnode =
linkedlist[Current].nextnode Here, Current tells us where the next node in the
chain is, so we can link the Previous node to it.

4. To update the Free List

When a node is deleted, that space in the array is now "Free." We need to tell
the FreePointer exactly which index is now available. FreePointer = Current This
says: "The index we just stopped at is now the start of the empty spaces.


