function parseConsentCookie(){
  var activeGroups = [];
  var cookieName = "OptanonConsent";
  var cookieValue;
  var groupsValue;
  var groupsValueDecoded;

  cookieValue = document.cookie
    .split("; ")
    .find(function(item){
      return item.startsWith(cookieName +'=')
    });
  
  if (cookieValue) {
    groupsValue = cookieValue
    .split("&")
    .find(function(pair){
      return pair.startsWith("groups=")
    })
    .split("=")[1];
  }

  if (groupsValue) {
    groupsValueDecoded = decodeURIComponent(groupsValue);
  }  

  if (groupsValueDecoded) {
    if(groupsValueDecoded.indexOf('C0001:1') > -1){
      activeGroups.push('C0001');
    }
    if(groupsValueDecoded.indexOf('C0002:1') > -1){
      activeGroups.push('C0002');
    }
    if(groupsValueDecoded.indexOf('C0003:1') > -1){
      activeGroups.push('C0003');
    }
    if(groupsValueDecoded.indexOf('C0004:1') > -1){
      activeGroups.push('C0004');
    }
  }

  return activeGroups && activeGroups.length > 0 ? activeGroups.join(',') : undefined;  
}
