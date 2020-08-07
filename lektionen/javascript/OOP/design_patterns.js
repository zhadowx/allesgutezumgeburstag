//Anti-pattern
function Car() {}
function BMW() {}
var engines = 1;
var features = {
  seats: 6,
  airbags: 6
};

//Single global object
var CARFACTORY = CARFACTORY || {};
CARFACTORY.Car = function() {};
CARFACTORY.BMW = function() {};
CARFACTORY.engines = 1;
CARFACTORY.features = {
  seats: 6,
  airbags: 6
};
//By convention the global namespace object is written in 
//all caps.

//Module Pattern
var basicServerConfig = {
  environment: "production",
  startupParams: {
    cacheTimeout: 30,
    locale: "en_US"
  },
  init: function() {
    console.log("Initializing the server");
  },
  updateStartup: function(params) {
    this.startupParams = params;  
    console.log(this.startupParams.cacheTimeout);
    console.log(this.startupParams.locale);    
  }
};
basicServerConfig.init(); //"Initializing the server"
basicServerConfig.updateStartup({cacheTimeout: 60,
locale: "en_UK"}); //60, en_UK
//--------------------------------------------------------

var basicServerConfig = (function() {
  var environment = "production";
  startupParams = {
    cacheTimeout: 30;
    locale: "en_US"
  };
  return {
    init: function() {
      console.log("Initializing the server");
    },
    updateStartup: function(params) {
      this.startupParams = params;
      console.log(this.startupParams.cacheTimeout);
      console.log(this.startupParams.locale);
    }
  };
})();
basicServerConfig.init(); //"Initializing the server"
basicServerConfig.updateStartup({cacheTimeout: 60,
locale: "en_UK"}); //60, en_UK
//---------------------------------------------------------
//Single global object
var SERVER = SERVER || {};
SERVER.basicServerConfig = (function() {
  var environment = "production";
  startupParams = {
    cacheTimeout: 30;
    locale: "en_US"
  };
  return {
    init: function() {
      console.log("Initializing the server");
    },
    updateStartup: function(params) {
      this.startupParams = params;
      console.log(this.startupParams.cacheTimeout);
      console.log(this.startupParams.locale);
    }
  };
})();
SERVER.basicServerConfig.init(); //"Initializing the server"
SERVER.basicServerConfig.updateStartup({cacheTimeout: 60,
locale: "en_UK"}); //60, en_UK
//--------------------------------------------------------------
//Example of a revealing module pattern (RMP)

var modulePattern = functin() {
  var privateOne = 1;
  function privateFn() {
    console.log('privateFn called');
  }
  return {
    publicTwo: 2,
    publicFn: function() {
      modulePattern.publicFnTwo();
    },
    publicFnTwo: function() {
      privateFn();
    }
  }
}();
modulePattern.publicFn(); //"privateFn called"
//-------------------------------------------------------------
//RMP primary idea is to define all of the members in the private 
//functionality that needs to be revealed as public

var revealingExample = function() {
  var privateOne = 1;
  function privateFn() {
    console.log('privateFn called');
  }
  var publicTwo = 2;
  function publicFn() {
    publicFnTwo();
  }
  function publicFnTwo() {
    privateFn();
  }
  function getCurrentState() {
    return 2;
  }
  //reveal private variables by assigning public pointers
  return {
    setup: publicFn,
    count: publicTwo,
    increaseCount: publicFnTwo,
    current: getCurrentState()
  };
}();
console.log(revealingExample.current); //2
revealingExample.setup(); //privateFn called
