import brightness from '../../services/brightness.js'
const audio = await Service.import('audio')
const network = await Service.import('network')
import { sep } from '../lib.js'

var wait = false

// Instance for brightness and volume indicators
const Brightness = () => {
    const revealer = Widget.Revealer({
        transitionDuration: 350,
        transition: 'slide_right',
        child: Widget.Slider({
            class_name: 'scale',
            hexpand: true,
            draw_value: false,
            step: 0.02,
            onChange: ({ value }) => {
                // Makes the slider smoother by reducing update events when scrolling
                if (!wait)
                    brightness.screen_value = value
                wait = !wait
            },
            setup: (self) => self.on('button-press-event', () => wait = false)
        })
    })
    return Widget.EventBox({
        on_hover: () => { revealer.child.value = brightness.screen_value; revealer.reveal_child = true },
        on_hover_lost: () => { revealer.reveal_child = false },
        child: Widget.Box({
            children: [
                revealer,
                Widget.Label({
                    class_name: 'icon',
                    css: 'padding-right: 8px;font-size: 18px;',
                    label: ''
                }),
            ],
        })
    })
}

const Volume = () => {
    const revealer = Widget.Revealer({
        transitionDuration: 350,
        transition: 'slide_right',
        child: Widget.Slider({
            class_name: 'scale',
            hexpand: true,
            drawValue: false,
            step: 0.01,
            onChange: ({ value }) => audio['speaker'].volume = value,
            value: audio['speaker'].bind('volume'),
        })
    })
    return Widget.EventBox({
        on_hover: () => { revealer.reveal_child = true },
        on_hover_lost: () => { revealer.reveal_child = false },
        child: Widget.Box({
            children: [
                revealer,
                Widget.Button({
                    on_clicked: () => audio.speaker.is_muted = !audio.speaker.is_muted,
                    child: Widget.Label({
                        class_name: 'icon',
                        css: 'padding-right: 4px;font-size: 20px;',
                        setup: (self) => self.hook(audio.speaker, self => {
                            const vol = audio.speaker.volume * 100;
                            const icon = [
                                [67, '󰕾'],
                                [34, '󰖀'],
                                [1, '󰕿'],
                                [0, '󰖁'],
                                // @ts-ignore
                            ].find(([threshold]) => threshold <= vol)?.[1];
                            self.label = `${icon}`
                        })
                    }),
                })
            ],
        })
    })
}

export const Network = () => {
    return Widget.EventBox({
        child: Widget.Box({
            children: [
                Widget.Button({
                    child: Widget.Label({
                        class_name: 'icon',
                        css: 'padding-right: 17px;',
                        label: ''
                    })
                }),
                Widget.Label({
                    class_name: 'txt-low',
                    setup: (self) => self.hook(network, self => {
                        const primary = network.primary == null ? 'wifi' : network.primary
                        const state = network[primary].state
                        const icon = [
                            ['disconected', 'offline'],
                            ['connected', 'online'],
                            // @ts-ignore
                        ].find(([threshold]) => threshold <= state)?.[1];
                        self.label = `${icon}`
                    })
                })
            ],
        })
    })
}

export const Resources = () => {
    return Widget.Box({
        spacing: 10,
        children: [
            Widget.Label({
                class_name: 'icon',
                label: '󰍛'
            }),
            Widget.Box({
                orientation: 1,
                vpack: 'center',
                spacing: 5,
                children: [
                    Widget.ProgressBar({
                        class_name: 'prog-bar',
                        setup: (self) => self
                            .poll(2000, () => Utils.execAsync(['bash', '-c', `top -bn1 | grep Cpu | awk '{print $2}'`])
                                .then((output) => {
                                    self.value = Math.round(Number(output)) / 100
                                })
                            )
                    }),
                    Widget.ProgressBar({
                        class_name: 'prog-bar',
                        setup: (self) => self
                            .poll(2000, () => Utils.execAsync(['bash', '-c', `free | awk '/^Mem/ {printf("%.2f\\n", ($3/$2) * 100)}'`])
                                .then((output) => {
                                    self.value = Math.round(Number(output)) / 100
                                })
                            )
                    })
                ]
            })
        ]
    })
}

export const Indicators = () => Widget.Box({
    class_name: 'module',
    spacing: 8,
    children: [
        Brightness(),
        sep(),
        Volume(),
        sep(),
        Network(),
        sep(),
        Resources(),
    ]
})
