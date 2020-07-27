//Modules
var moduleName = function() {
  //private state
  //private functions
  return {
    //public state
    //public variables
  }
}

var superModule = (function () {
  var secret = 'supersecretkey';
  var passcode = 'nuke';

  function getSecret() {
    console.log(secret);
  }

  function getPassCode() {
    console.log(passcode);
  }
  return {
    getSecret: getSecret,
    getPassCode: getPassCode
  };
})();
superModule.getSecret();
superModule.getPassCode();
