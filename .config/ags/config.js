import Gio from 'gi://Gio'
import { Bar } from './widgets/bar/main.js'

function applyStyle() {
    console.log('Applying styles ...')
    Utils.execAsync(`sassc ${App.configDir}/scss/main.scss ${App.configDir}/style.css`)
        .then(out => print(out))
        .catch(err => print(err));
    App.resetCss()
    App.applyCss(`${App.configDir}/style.css`)
    console.log('Styles loaded !')
    Utils.notify({
        summary: '[AGS] Styles loaded',
        timeout: 3000,
    })
}

// A better approach for triggering changes event (only laods changes one time instead of multiple random times)
Utils.monitorFile(`${App.configDir}/scss`, (_, eventType) => {
    if (eventType === Gio.FileMonitorEvent.CHANGED) {
        applyStyle()
    }
});

applyStyle();
export default {
    stackTraceOnError: true,
    windows: [await Bar()]
}
