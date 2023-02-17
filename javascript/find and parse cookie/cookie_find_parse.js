const cookieName = "OptanonConsent";
const cookieValue = document.cookie.split("; ")
  .find(cookie => cookie.startsWith(`${cookieName}=`))
  .split("=")[1];

const groupsValue = cookieValue.split("&").find(pair => pair.startsWith("groups=")).split("=")[1];

const containsC00021 = groupsValue.includes("C0002:1");
const containsC00020 = groupsValue.includes("C0002:0");

if (containsC00021) {
  return true;
} else if (containsC00020) {
  return false;
} else {
  // handle case where neither substring is present
}
