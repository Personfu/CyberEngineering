/* Original, minimal external-app example. Build in a matching official Flipper SDK. */
#include <furi.h>

int32_t nightshift_hello_app(void* context) {
    UNUSED(context);
    FURI_LOG_I("Nightshift", "Hello from an owned local application");
    return 0;
}
