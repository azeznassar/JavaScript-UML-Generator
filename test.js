class Cat {
    constructor(catName, catAge) {
      this.catName = 0;
      this.catAge = "test-string";
    }
    
    speak() {
      console.log(`${this.catName} makes a noise.`);
    }

    displayAge() {
      console.log(`${this.catName} is ${this.catAge}.`);
    }
}

class Dog {
  constructor(dogName, dogAge) {
    this.dogName = dogName;
    this.dogAge = dogAge;
  }
  
  speak() {
    console.log(`${this.dogName} makes a noise.`);
  }

  displayAge() {
    console.log(`${this.dogName} is ${this.dogAge}.`);
  }
}