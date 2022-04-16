import { boot } from "quasar/wrappers";
import { createI18n } from "vue-i18n";

import messages from "../i18n";
import numberFormats from "../i18n/numberFormats";

export default boot(({ app }) => {
  const i18n = createI18n({
    locale: "en-AU",
    fallbackLocale: "en-AU",
    numberFormats,
    messages,
  });

  // Set i18n instance on app
  app.use(i18n);
});
