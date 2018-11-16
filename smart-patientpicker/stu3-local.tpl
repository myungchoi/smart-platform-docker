{
    server: {
        // "DSTU-2" or "STU-3"
        type: "STU-3",

        // Api URL
        url: "https://apps.hdap.gatech.edu/gt-fhir/fhir",

        // The pre-populated tags in the tag selector
        tags: [
        ],

        // The medical conditions available on this server
        conditions: {
        }
    },

    // Records per page
    patientsPerPage: 25,

    // AJAX requests timeout (ms)
    timeout: 20000,

    // Only the selected patients are rendered. Should be false or the
    // preselected patient IDs should be passed to the window. Otherwise
    // It will result in rendering no patients at all.
    renderSelectedOnly: false,

    // If enabled is true (then url and param MUST be set) then clicking on the
    // patient-related resources in detail view will open their source in that
    // external viewer. Otherwise they will just be opened in new browser tab.
    fhirViewer: {
        enabled: true,
        url    : "http://docs.smarthealthit.org/fhir-viewer/index.html",
        param  : "url"
    },

    // What to send when the OK dialog button is clicked. Possible values:
    // "id-list"  - comma-separated list of patient IDs (default)
    // "id-array" - array of patient IDs
    // "patients" - array of patient JSON objects
    outputMode: "id-list",

    // "automatic" -> onChange plus defer in some cases
    // "manual" -> render a submit button
    submitStrategy: "manual"
}