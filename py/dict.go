// Dict and StringDict type
//
// The idea is that most dicts just have strings for keys so we use
// the simpler StringDict and promote it into a Dict when necessary

package py

var StringDictType = NewType("dict", "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)")

var DictType = NewType("dict", "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)")

// String to object dictionary
//
// Used for variables etc where the keys can only be strings
type StringDict map[string]Object

// Type of this StringDict object
func (o StringDict) Type() *Type {
	return StringDictType
}

// Make a new dictionary
func NewStringDict() StringDict {
	return make(StringDict)
}

// Make a new dictionary with reservation for n entries
func NewStringDictSized(n int) StringDict {
	return make(StringDict, n)
}

// Copy a dictionary
func (d StringDict) Copy() StringDict {
	e := make(StringDict, len(d))
	for k, v := range d {
		e[k] = v
	}
	return e
}

func (d StringDict) M__getitem__(key Object) (Object, error) {
	str, ok := key.(String)
	if ok {
		res, ok := d[string(str)]
		if ok {
			return res, nil
		}
	}
	return nil, ExceptionNewf(KeyError, "%v", key)
}

func (d StringDict) M__setitem__(key, value Object) (Object, error) {
	str, ok := key.(String)
	if !ok {
		return nil, ExceptionNewf(KeyError, "FIXME can only have string keys!: %v", key)
	}
	d[string(str)] = value
	return None, nil
}

func (a StringDict) M__eq__(other Object) (Object, error) {
	b, ok := other.(StringDict)
	if !ok {
		return NotImplemented, nil
	}
	if len(a) != len(b) {
		return False, nil
	}
	for k, av := range a {
		bv, ok := b[k]
		if !ok {
			return False, nil
		}
		res, err := Eq(av, bv)
		if err != nil {
			return nil, err
		}
		if res == False {
			return False, nil
		}
	}
	return True, nil
}

func (a StringDict) M__ne__(other Object) (Object, error) {
	res, err := a.M__eq__(other)
	if err != nil {
		return nil, err
	}
	if res == True {
		return False, nil
	}
	return True, nil
}
