// listen custom event and fire dataLayer event
window.addEventListener('analytics', function(event) {
  try {
    var originalEventName = event.detail.originalEventType;
    var originalEventInfo = event.detail.originalEventDetail;
    if (originalEventName == 'add-to-basket') {      
      console.log('*** Analytics event captured \n\tevent:', originalEventName);
      window.dataLayer.push(
        Object.assign({}, {event: 'gtm-add-to-basket'}, originalEventInfo)
      );
    }
  } catch (e) {
  }
});

// dispatch custom event
var newEvent = new CustomEvent('gtm-context-data-ready', { detail: {a: 'aa', b: 'bb'} });
window.dispatchEvent(newEvent);
