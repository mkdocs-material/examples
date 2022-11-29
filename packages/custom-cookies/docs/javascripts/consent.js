var consent = __md_get("__consent")
if (consent && consent.custom) {
  /* The user accepted the cookie */
  alert$.next("Custom cookie was accepted")
}
