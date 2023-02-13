// define dataLayer first
var datalayerName = 'dataLayer';
window[datalayerName] = window[datalayerName] || [];

// list of events to be tested
var eventList = [
  {"event":"bambuser-video-shopping", "type":"show-started","isLive":false,"showId":"V1VjoIheodJIJRCkNPUH","showTimeWatched":"0/1","showTitle":"Test 2"},
  {"event":"bambuser-video-shopping", "type":"add-to-basket","isLive":false,"showId":"V1VjoIheodJIJRCkNPUH","showTimeWatched":"10/361","showTitle":"Test 2","itemCode":"1276","localName":"Tender Care Protecting Balm","placement":"bambuser-video","quantity":1},
  {"event":"bambuser-video-shopping", "type":"like-button-clicked","isLive":false,"showId":"V1VjoIheodJIJRCkNPUH","showTimeWatched":"28/361","showTitle":"Test 2"},
  {"event":"bambuser-video-shopping", "type":"show-ended","isLive":false,"showId":"V1VjoIheodJIJRCkNPUH","showTimeWatched":"1/1","showTitle":"Test 2"},
];

// loop pushes with interval timer
function dlEventLoopPusher() {
  var index = 0;
  var timer = setInterval(dlEventPusher, 1100);
  function dlEventPusher() {
    if (index == eventList.length) {
      clearInterval(timer);
    } else {        
      window[datalayerName].push( eventList[index] );
      index++;
    }
  }
}
// start pushing:
dlEventLoopPusher();


/************************************ */
/* pushes without interval timer */
var eventList = [
    'begin_checkout',
    'cartAdd',
    'checkout_progress',
    'download',
    'ecommerceTransaction',
    'filter',
    'login',
    'outbound_link',
    'productClick',
    'productDetailView',
    'productImpression',
    'promotionClick',
    'promotionView',
    'registerConsultant',
    'remove_from_cart',
    'search',
    'share',
    'sort',
    'test_event',
    'userRegistered',
    'userUpgraded',
    'virtualPageView'
];

var datalayerName = 'dataLayer';
window[datalayerName] = window[datalayerName] || [];

eventList.forEach(function(item, index) { window[datalayerName].push({'event' : item}); });
