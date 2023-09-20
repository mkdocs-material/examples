var consent = __md_get("__consent")
if (consent) {
  if (consent.custom) {
    alert$.next("Custom cookie was accepted")
  } else {
    alert$.next("Custom cookie was rejected")
  }
}
