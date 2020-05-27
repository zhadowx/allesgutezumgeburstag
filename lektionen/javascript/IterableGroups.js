class Group {
  constructor() {
    this.members = [];
  }

  has(value) {
    return this.members.includes(value);
  }

  add(value) {
    if (!this.has(value)) {
      this.members.push(value);
    }
  }

  delete(value) {
    this.members = this.members.filter(v => v !== value);  
  }

  static from(collection) {
    let group = new Group;
    collection.forEach(value => group.add(value));
    return group;
  }

  [Symbol.iterator]() {
    return new GroupIterator(this);
  }

}


class GroupIterator {
  constructor(group) {
    this.group = group;
    this.x = 0;
  }

  next() {
    if (this.x >= this.group.members.length) {
      return {done: true};
    } 
    else {
      let result = {value: this.group.members[this.x], done: false};
      this.x++;
      return result;
    }
  }
}


for (let value of Group.from(["a", "b", "c"])) {
  console.log(value);
}