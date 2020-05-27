class Group {
  constructor() {
    this.members = [];
  }

  has(x) {
    return this.members.includes(x);
  }

  add(x) {
    if (!this.has(x)) {
      this.members.push(x);
    }
  }

  delete(x) {
    this.members = this.members.filter(y => y !== x);  
  }

  static from(collection) {
    let group = new Group;
    collection.forEach(x => group.add(x));
    return group;
  }
}

let group = Group.from([10, 20]);
console.log(group.has(10));
// → true
console.log(group.has(30));
// → false
group.add(10);
group.delete(10);
console.log(group.has(10));
// → false