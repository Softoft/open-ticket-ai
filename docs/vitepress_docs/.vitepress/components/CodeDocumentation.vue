<template>
    <!-- RENDER A LIST OF SUB-PACKAGES -->
    <div v-if="subPackagesToDisplay.length > 0" class="sub-package-container">
        <h2 class="mb-4">
            <CodeBadge text="package" type="success"/>
            <span class="font-monospace">Contents of {{ parentPackageId }}</span>
        </h2>
        <div class="d-grid gap-4">
            <div v-for="subPkg in subPackagesToDisplay" :key="subPkg.module_path">
                <!-- Recursively call the component to render each sub-module as a full card -->
                <CodeDocumentation
                    :package-id="subPkg.module_path"
                    show-all-classes
                    show-all-functions
                />
            </div>
        </div>
    </div>

    <!-- RENDER A SINGLE DOC ITEM (class or package) -->
    <div v-else-if="classData || packageData" class="code-documentation-wrapper card shadow-sm mb-4">
        <!-- RENDER A SINGLE CLASS -->
        <div v-if="classData" class="card-body">
            <h2 class="card-title mb-1">
                <CodeBadge text="class" type="warning"/>
                <span class="font-monospace">{{ classData.name }}</span>
            </h2>
            <p class="card-subtitle mb-2 text-muted small">
                From: <code>{{ classData.module_path }}</code>
            </p>
            <Docstring :doc="classData.docstring"/>

            <!-- Methods Section -->
            <div v-if="methodsToDisplay.length > 0" class="mt-4">
                <h3>Methods</h3>
                <div :id="`accordion-methods-${classId}`" class="accordion">
                    <FunctionDoc v-for="method in methodsToDisplay" :key="method.name" :func="method"
                                 :parent-id="classId"/>
                </div>
            </div>
        </div>

        <!-- RENDER A WHOLE PACKAGE/MODULE -->
        <div v-if="packageData" class="card-body">
            <h3 class="card-title mb-1">
                <CodeBadge text="module" type="primary"/>
                <span class="font-monospace">{{ packageId }}</span>
            </h3>
            <Docstring :doc="packageData.module_docstring"/>

            <!-- All Classes in Package -->
            <div v-if="showAllClasses && packageData.classes.length > 0" class="mt-4">
                <h4>Classes</h4>
                <div v-for="cls in packageData.classes" :key="cls.name" class="mb-3">
                    <CodeDocumentation :class_id="`${packageId.replace(/\//g, '.')}.${cls.name}`" show-public-methods/>
                </div>
            </div>

            <!-- All Functions in Package -->
            <div v-if="showAllFunctions && packageData.functions.length > 0" class="mt-4">
                <h4>Functions</h4>
                <div :id="`accordion-functions-${packageId}`" class="accordion">
                    <FunctionDoc v-for="func in packageData.functions" :key="func.name" :func="func"
                                 :parent-id="packageId"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {computed} from 'vue';
// Import ModuleEntry for the new computed property
import {useApiDocs} from '../composables/useApiDocs';
import FunctionDoc from './FunctionDoc.vue';
import Docstring from './Docstring.vue';
import CodeBadge from './CodeBadge.vue';

// Define the component's props with types
interface Props {
    classId?: string;
    packageId?: string;
    parentPackageId?: string; // <-- NEW PROP
    showAllMethods?: boolean;
    showPublicMethods?: boolean;
    showPublicAttributes?: boolean; // For future use
    showAllClasses?: boolean;
    showAllFunctions?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
    classId: '',
    packageId: '',
    parentPackageId: '', // <-- NEW PROP DEFAULT
    showAllMethods: false,
    showPublicMethods: false,
    showPublicAttributes: false,
    showAllClasses: false,
    showAllFunctions: false,
});

// Get the processed data from our store
const {packages, classes} = useApiDocs();

// Find the specific data based on the ID props, with types for the computed values
const classData = computed(() => props.classId ? (classes.get(props.classId) ?? null) : null);
const packageData = computed(() => props.packageId ? (packages.get(props.packageId) ?? null) : null);


// Computed property to dynamically filter methods
const methodsToDisplay = computed(() => {
    if (!classData.value?.methods) return [];
    if (props.showAllMethods) {
        return classData.value.methods;
    }
    if (props.showPublicMethods) {
        // Public methods in Python don't start with an underscore
        return classData.value.methods.filter(method => !method.name.startsWith('_'));
    }
    return [];
});

// NEW computed property to find sub-packages
const subPackagesToDisplay = computed(() => {
    if (!props.parentPackageId) return [];

    const allPackages = Array.from(packages.values());
    // Normalize module paths to use dots for consistent matching
    const parentPath = props.parentPackageId.replace(/\//g, '.');

    return allPackages.filter(pkg => {
        const childPath = pkg.module_path.replace(/\//g, '.');
        // Find modules that are children of the parent package
        return childPath.startsWith(parentPath + '.')
    });
});
</script>

<style scoped>
.code-documentation-wrapper {
    /* The VP theme provides a --vp-c-bg-soft for a subtle background. */
    background-color: var(--vp-c-bg-soft, #f8f9fa);
}

.card-title .font-monospace {
    color: var(--vp-c-brand-1);
}
</style>
