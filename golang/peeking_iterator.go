package golang

/*   Below is the interface for Iterator, which is already defined for you.
 *
 *   type Iterator struct {
 *
 *   }
 *
 *   func (this *Iterator) hasNext() bool {
 *		// Returns true if the iteration has more elements.
 *   }
 *
 *   func (this *Iterator) next() int {
 *		// Returns the next element in the iteration.
 *   }
 */

// PeekingIterator is struct for PeekingIterator class
type PeekingIterator struct {
    Iter *Iterator
    Next int
    HasPeeked bool
}

// PeekingIteratorConstructor object constructor
func PeekingIteratorConstructor(iter *Iterator) *PeekingIterator {
    obj := &PeekingIterator{
        Iter: iter,
        HasPeeked: false,
    }
    
    return obj
}

func (obj *PeekingIterator) hasNext() bool {
    return obj.HasPeeked || obj.Iter.hasNext()
}

func (obj *PeekingIterator) next() int {
    if !obj.HasPeeked {
        obj.Next = obj.Iter.next()
    }
    obj.HasPeeked = false
    
    return obj.Next
}

func (obj *PeekingIterator) peek() int {
    if !obj.HasPeeked {
        obj.Next = obj.Iter.next()
    }
    obj.HasPeeked = true
    
    return obj.Next
}