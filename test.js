class Cat {
    constructor (catName, catAge) {
      this.catName = ''
      this.catAge = 20
    }
  
    speak (words) {
      let dog = new Dog('Name', 123)
  
      return 34
    }
  
    displayAge () {
      console.log(`${this.catName} is ${this.catAge}.`)
    }
  }
  
  class Animal {
    constructor (name, age, isADog) {
      this.dogName = 'test-string'
      this.dogAge = 0
      this.isADog = false
    }
  
    walk () {
      console.log('walking')
    }
  }
  
  class Dog extends Animal {
    constructor (dogName, dogAge) {
      this.dogName = 'test-string'
      this.dogAge = 0
    }
  
    speak () {
      console.log(`${this.dogName} makes a noise.`)
  
      return 'MyString'
    }
  
    displayAge () {
      console.log(`${this.dogName} is ${this.dogAge}.`)
    }
  }