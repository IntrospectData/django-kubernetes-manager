---
title: DKM API
language_tabs:
  - python: Python
toc_footers: []
includes: []
search: false
highlight_theme: darkula
headingLevel: 2

---

<h1 id="dkm-api">DKM API v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Django Kubernetes Manager

Base URLs:

* <a href="http://127.0.0.1:8000/api">http://127.0.0.1:8000/api</a>

<a href="https://introspectdata.com/terms-service/">Terms of service</a>
Email: <a href="mailto:bradley@introspectdata.com">Support</a> 
License: <a href="https://github.com/IntrospectData/Django-Kubernetes-Manager/blob/master/LICENSE">MIT License</a>

# Authentication

- HTTP Authentication, scheme: basic 

<h1 id="dkm-api-clusters">clusters</h1>

## clusters_list

<a id="opIdclusters_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/clusters/', params={

}, headers = headers)

print r.json()

```

`GET /clusters/`

API endpoint that allows cluster configs to be edited or deleted

<h3 id="clusters_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "api_endpoint": "http://example.com",
      "telemetry_endpoint": "http://example.com",
      "config": {}
    }
  ]
}
```

<h3 id="clusters_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="clusters_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[TargetCluster](#schematargetcluster)]|true|none|none|
|»» title|string|true|none|none|
|»» api_endpoint|string(uri)|true|none|Cluster Endpoint URL|
|»» telemetry_endpoint|string(uri)|true|none|Telemetry Endpoint URL|
|»» config|object\|null|false|none|Configuration data stored as an encrypted blob in the database|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## clusters_create

<a id="opIdclusters_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/clusters/', params={

}, headers = headers)

print r.json()

```

`POST /clusters/`

API endpoint that allows cluster configs to be edited or deleted

> Body parameter

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TargetCluster](#schematargetcluster)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[TargetCluster](#schematargetcluster)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## clusters_read

<a id="opIdclusters_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/clusters/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /clusters/{id}/`

API endpoint that allows cluster configs to be edited or deleted

<h3 id="clusters_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this target cluster.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[TargetCluster](#schematargetcluster)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## clusters_update

<a id="opIdclusters_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/clusters/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /clusters/{id}/`

API endpoint that allows cluster configs to be edited or deleted

> Body parameter

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TargetCluster](#schematargetcluster)|true|none|
|id|path|integer|true|A unique integer value identifying this target cluster.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[TargetCluster](#schematargetcluster)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## clusters_partial_update

<a id="opIdclusters_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/clusters/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /clusters/{id}/`

API endpoint that allows cluster configs to be edited or deleted

> Body parameter

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[TargetCluster](#schematargetcluster)|true|none|
|id|path|integer|true|A unique integer value identifying this target cluster.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}
```

<h3 id="clusters_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[TargetCluster](#schematargetcluster)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## clusters_delete

<a id="opIdclusters_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/clusters/{id}/', params={

)

print r.json()

```

`DELETE /clusters/{id}/`

API endpoint that allows cluster configs to be edited or deleted

<h3 id="clusters_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer|true|A unique integer value identifying this target cluster.|

<h3 id="clusters_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-containers">containers</h1>

## containers_list

<a id="opIdcontainers_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/containers/', params={

}, headers = headers)

print r.json()

```

`GET /containers/`

API endpoint that allows containers to be edited or deleted.

<h3 id="containers_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "image_name": "string",
      "image_tag": "string",
      "image_pull_policy": "Always",
      "command": "string",
      "args": "string",
      "port": -2147483648,
      "volume_mount": "http://example.com"
    }
  ]
}
```

<h3 id="containers_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="containers_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesContainer](#schemakubernetescontainer)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» image_name|string|false|none|Properly qualified image name to execute this job within|
|»» image_tag|string|false|none|Tag name for the image to be used for this job|
|»» image_pull_policy|string|false|none|none|
|»» command|string\|null|false|none|Command to run when instantiating container|
|»» args|string\|null|false|none|Comma separated args to run with command when instantiating container.|
|»» port|integer|false|none|none|
|»» volume_mount|string(uri)\|null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|image_pull_policy|Always|
|image_pull_policy|IfNotPresent|
|image_pull_policy|Never|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## containers_create

<a id="opIdcontainers_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/containers/', params={

}, headers = headers)

print r.json()

```

`POST /containers/`

API endpoint that allows containers to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesContainer](#schemakubernetescontainer)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesContainer](#schemakubernetescontainer)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## containers_read

<a id="opIdcontainers_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/containers/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /containers/{id}/`

API endpoint that allows containers to be edited or deleted.

<h3 id="containers_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes container.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesContainer](#schemakubernetescontainer)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## containers_update

<a id="opIdcontainers_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/containers/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /containers/{id}/`

API endpoint that allows containers to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesContainer](#schemakubernetescontainer)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes container.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesContainer](#schemakubernetescontainer)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## containers_partial_update

<a id="opIdcontainers_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/containers/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /containers/{id}/`

API endpoint that allows containers to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesContainer](#schemakubernetescontainer)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes container.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}
```

<h3 id="containers_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesContainer](#schemakubernetescontainer)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## containers_delete

<a id="opIdcontainers_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/containers/{id}/', params={

)

print r.json()

```

`DELETE /containers/{id}/`

API endpoint that allows containers to be edited or deleted.

<h3 id="containers_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes container.|

<h3 id="containers_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-deployments">deployments</h1>

## deployments_list

<a id="opIddeployments_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/deployments/', params={

}, headers = headers)

print r.json()

```

`GET /deployments/`

API endpoint that allows deployments to be edited or deleted.

<h3 id="deployments_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "api_version": "string",
      "kind": "string",
      "port": -2147483648,
      "namespace": "string",
      "kuid": "string",
      "selector": {},
      "replicas": -2147483648,
      "pod_template": "http://example.com"
    }
  ]
}
```

<h3 id="deployments_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="deployments_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesDeployment](#schemakubernetesdeployment)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» api_version|string|false|none|none|
|»» kind|string|true|none|none|
|»» port|integer|false|none|none|
|»» namespace|string|false|none|none|
|»» kuid|string\|null|false|none|Object's UID in the cluster|
|»» selector|object|false|none|none|
|»» replicas|integer|false|none|none|
|»» pod_template|string(uri)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_create

<a id="opIddeployments_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/deployments/', params={

}, headers = headers)

print r.json()

```

`POST /deployments/`

API endpoint that allows deployments to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_read

<a id="opIddeployments_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/deployments/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /deployments/{id}/`

API endpoint that allows deployments to be edited or deleted.

<h3 id="deployments_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_update

<a id="opIddeployments_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/deployments/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /deployments/{id}/`

API endpoint that allows deployments to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_partial_update

<a id="opIddeployments_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/deployments/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /deployments/{id}/`

API endpoint that allows deployments to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_delete

<a id="opIddeployments_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/deployments/{id}/', params={

)

print r.json()

```

`DELETE /deployments/{id}/`

API endpoint that allows deployments to be edited or deleted.

<h3 id="deployments_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

<h3 id="deployments_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_deploy_read

<a id="opIddeployments_deploy_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/deployments/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`GET /deployments/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

<h3 id="deployments_deploy_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_deploy_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_deploy_create

<a id="opIddeployments_deploy_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/deployments/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`POST /deployments/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_deploy_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_deploy_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_k_delete_read

<a id="opIddeployments_k_delete_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/deployments/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`GET /deployments/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespaces

<h3 id="deployments_k_delete_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_k_delete_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_k_delete_create

<a id="opIddeployments_k_delete_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/deployments/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`POST /deployments/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespaces

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_k_delete_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_k_delete_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_pod_usage_read

<a id="opIddeployments_pod_usage_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/deployments/{id}/pod_usage/', params={

}, headers = headers)

print r.json()

```

`GET /deployments/{id}/pod_usage/`

Action to fetch point-in-time cpu and memory usage of pod.

<h3 id="deployments_pod_usage_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_pod_usage_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## deployments_pod_usage_create

<a id="opIddeployments_pod_usage_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/deployments/{id}/pod_usage/', params={

}, headers = headers)

print r.json()

```

`POST /deployments/{id}/pod_usage/`

Action to fetch point-in-time cpu and memory usage of pod.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_pod_usage_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesDeployment](#schemakubernetesdeployment)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes deployment.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="deployments_pod_usage_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesDeployment](#schemakubernetesdeployment)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-ingresses">ingresses</h1>

## ingresses_list

<a id="opIdingresses_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/ingresses/', params={

}, headers = headers)

print r.json()

```

`GET /ingresses/`

API endpoint that allows ingress to be edited or deleted.

<h3 id="ingresses_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "api_version": "string",
      "kind": "string",
      "port": -2147483648,
      "namespace": "string",
      "kuid": "string",
      "hostname": "string",
      "path": "string",
      "target_service": "http://example.com"
    }
  ]
}
```

<h3 id="ingresses_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="ingresses_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesIngress](#schemakubernetesingress)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» api_version|string|false|none|none|
|»» kind|string|true|none|none|
|»» port|integer|false|none|none|
|»» namespace|string|false|none|none|
|»» kuid|string\|null|false|none|Object's UID in the cluster|
|»» hostname|string|false|none|none|
|»» path|string|false|none|none|
|»» target_service|string(uri)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_create

<a id="opIdingresses_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/ingresses/', params={

}, headers = headers)

print r.json()

```

`POST /ingresses/`

API endpoint that allows ingress to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesIngress](#schemakubernetesingress)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_read

<a id="opIdingresses_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/ingresses/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /ingresses/{id}/`

API endpoint that allows ingress to be edited or deleted.

<h3 id="ingresses_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_update

<a id="opIdingresses_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/ingresses/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /ingresses/{id}/`

API endpoint that allows ingress to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesIngress](#schemakubernetesingress)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_partial_update

<a id="opIdingresses_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/ingresses/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /ingresses/{id}/`

API endpoint that allows ingress to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesIngress](#schemakubernetesingress)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_delete

<a id="opIdingresses_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/ingresses/{id}/', params={

)

print r.json()

```

`DELETE /ingresses/{id}/`

API endpoint that allows ingress to be edited or deleted.

<h3 id="ingresses_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

<h3 id="ingresses_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_deploy_read

<a id="opIdingresses_deploy_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/ingresses/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`GET /ingresses/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

<h3 id="ingresses_deploy_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_deploy_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_deploy_create

<a id="opIdingresses_deploy_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/ingresses/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`POST /ingresses/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_deploy_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesIngress](#schemakubernetesingress)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_deploy_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_k_delete_read

<a id="opIdingresses_k_delete_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/ingresses/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`GET /ingresses/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespace.

<h3 id="ingresses_k_delete_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_k_delete_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## ingresses_k_delete_create

<a id="opIdingresses_k_delete_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/ingresses/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`POST /ingresses/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespace.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_k_delete_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesIngress](#schemakubernetesingress)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes ingress.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}
```

<h3 id="ingresses_k_delete_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesIngress](#schemakubernetesingress)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-jobs">jobs</h1>

## jobs_list

<a id="opIdjobs_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/jobs/', params={

}, headers = headers)

print r.json()

```

`GET /jobs/`

API endpoint that allows jobs to be edited or deleted.

<h3 id="jobs_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "api_version": "string",
      "kind": "string",
      "port": -2147483648,
      "namespace": "string",
      "kuid": "string",
      "backoff_limit": -2147483648,
      "pod_template": "http://example.com"
    }
  ]
}
```

<h3 id="jobs_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="jobs_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesJob](#schemakubernetesjob)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» api_version|string|false|none|none|
|»» kind|string|true|none|none|
|»» port|integer|false|none|none|
|»» namespace|string|false|none|none|
|»» kuid|string\|null|false|none|Object's UID in the cluster|
|»» backoff_limit|integer|false|none|none|
|»» pod_template|string(uri)|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_create

<a id="opIdjobs_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/jobs/', params={

}, headers = headers)

print r.json()

```

`POST /jobs/`

API endpoint that allows jobs to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_read

<a id="opIdjobs_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/jobs/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /jobs/{id}/`

API endpoint that allows jobs to be edited or deleted.

<h3 id="jobs_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_update

<a id="opIdjobs_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/jobs/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /jobs/{id}/`

API endpoint that allows jobs to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_partial_update

<a id="opIdjobs_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/jobs/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /jobs/{id}/`

API endpoint that allows jobs to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_delete

<a id="opIdjobs_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/jobs/{id}/', params={

)

print r.json()

```

`DELETE /jobs/{id}/`

API endpoint that allows jobs to be edited or deleted.

<h3 id="jobs_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

<h3 id="jobs_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_deploy_read

<a id="opIdjobs_deploy_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/jobs/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`GET /jobs/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

<h3 id="jobs_deploy_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_deploy_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_deploy_create

<a id="opIdjobs_deploy_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/jobs/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`POST /jobs/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_deploy_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_deploy_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_k_delete_read

<a id="opIdjobs_k_delete_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/jobs/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`GET /jobs/{id}/k_delete/`

Action to delete the kubernetes resource from the target cluster/ns.

<h3 id="jobs_k_delete_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_k_delete_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_k_delete_create

<a id="opIdjobs_k_delete_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/jobs/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`POST /jobs/{id}/k_delete/`

Action to delete the kubernetes resource from the target cluster/ns.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_k_delete_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_k_delete_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_pod_usage_read

<a id="opIdjobs_pod_usage_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/jobs/{id}/pod_usage/', params={

}, headers = headers)

print r.json()

```

`GET /jobs/{id}/pod_usage/`

Action to fetch point-in-time cpu and memory usage of pod.

<h3 id="jobs_pod_usage_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_pod_usage_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## jobs_pod_usage_create

<a id="opIdjobs_pod_usage_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/jobs/{id}/pod_usage/', params={

}, headers = headers)

print r.json()

```

`POST /jobs/{id}/pod_usage/`

Action to fetch point-in-time cpu and memory usage of pod.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_pod_usage_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesJob](#schemakubernetesjob)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes job.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}
```

<h3 id="jobs_pod_usage_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesJob](#schemakubernetesjob)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-namespaces">namespaces</h1>

## namespaces_list

<a id="opIdnamespaces_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/namespaces/', params={

}, headers = headers)

print r.json()

```

`GET /namespaces/`

API endpoint that allows namespaces to be created or deleted

<h3 id="namespaces_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "api_version": "string",
      "kind": "string",
      "exists": true
    }
  ]
}
```

<h3 id="namespaces_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="namespaces_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesNamespace](#schemakubernetesnamespace)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» api_version|string|false|none|none|
|»» kind|string|true|none|none|
|»» exists|boolean|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_create

<a id="opIdnamespaces_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/namespaces/', params={

}, headers = headers)

print r.json()

```

`POST /namespaces/`

API endpoint that allows namespaces to be created or deleted

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesNamespace](#schemakubernetesnamespace)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_read

<a id="opIdnamespaces_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/namespaces/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /namespaces/{id}/`

API endpoint that allows namespaces to be created or deleted

<h3 id="namespaces_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_update

<a id="opIdnamespaces_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/namespaces/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /namespaces/{id}/`

API endpoint that allows namespaces to be created or deleted

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesNamespace](#schemakubernetesnamespace)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_partial_update

<a id="opIdnamespaces_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/namespaces/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /namespaces/{id}/`

API endpoint that allows namespaces to be created or deleted

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesNamespace](#schemakubernetesnamespace)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_delete

<a id="opIdnamespaces_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/namespaces/{id}/', params={

)

print r.json()

```

`DELETE /namespaces/{id}/`

API endpoint that allows namespaces to be created or deleted

<h3 id="namespaces_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

<h3 id="namespaces_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_deploy_read

<a id="opIdnamespaces_deploy_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/namespaces/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`GET /namespaces/{id}/deploy/`

Action to deploy the namespace resource to target cluster.

<h3 id="namespaces_deploy_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_deploy_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_deploy_create

<a id="opIdnamespaces_deploy_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/namespaces/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`POST /namespaces/{id}/deploy/`

Action to deploy the namespace resource to target cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_deploy_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesNamespace](#schemakubernetesnamespace)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_deploy_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_k_delete_read

<a id="opIdnamespaces_k_delete_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/namespaces/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`GET /namespaces/{id}/k_delete/`

Action to delete the kubernetes namespace from the cluster.

<h3 id="namespaces_k_delete_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_k_delete_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## namespaces_k_delete_create

<a id="opIdnamespaces_k_delete_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/namespaces/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`POST /namespaces/{id}/k_delete/`

Action to delete the kubernetes namespace from the cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_k_delete_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesNamespace](#schemakubernetesnamespace)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes namespace.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}
```

<h3 id="namespaces_k_delete_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesNamespace](#schemakubernetesnamespace)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-pods">pods</h1>

## pods_list

<a id="opIdpods_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/pods/', params={

}, headers = headers)

print r.json()

```

`GET /pods/`

API endpoint that allows pod templates to be edited or deleted.

<h3 id="pods_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "volume": "http://example.com",
      "primary_container": "http://example.com",
      "secondary_container": "http://example.com",
      "restart_policy": "Always"
    }
  ]
}
```

<h3 id="pods_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="pods_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesPodTemplate](#schemakubernetespodtemplate)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» volume|string(uri)\|null|false|none|none|
|»» primary_container|string(uri)|true|none|none|
|»» secondary_container|string(uri)\|null|false|none|none|
|»» restart_policy|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|restart_policy|Always|
|restart_policy|OnFailure|
|restart_policy|Never|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## pods_create

<a id="opIdpods_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/pods/', params={

}, headers = headers)

print r.json()

```

`POST /pods/`

API endpoint that allows pod templates to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesPodTemplate](#schemakubernetespodtemplate)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesPodTemplate](#schemakubernetespodtemplate)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## pods_read

<a id="opIdpods_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/pods/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /pods/{id}/`

API endpoint that allows pod templates to be edited or deleted.

<h3 id="pods_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes pod template.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesPodTemplate](#schemakubernetespodtemplate)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## pods_update

<a id="opIdpods_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/pods/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /pods/{id}/`

API endpoint that allows pod templates to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesPodTemplate](#schemakubernetespodtemplate)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes pod template.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesPodTemplate](#schemakubernetespodtemplate)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## pods_partial_update

<a id="opIdpods_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/pods/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /pods/{id}/`

API endpoint that allows pod templates to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesPodTemplate](#schemakubernetespodtemplate)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes pod template.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}
```

<h3 id="pods_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesPodTemplate](#schemakubernetespodtemplate)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## pods_delete

<a id="opIdpods_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/pods/{id}/', params={

)

print r.json()

```

`DELETE /pods/{id}/`

API endpoint that allows pod templates to be edited or deleted.

<h3 id="pods_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes pod template.|

<h3 id="pods_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

<h1 id="dkm-api-services">services</h1>

## services_list

<a id="opIdservices_list"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/services/', params={

}, headers = headers)

print r.json()

```

`GET /services/`

API endpoint that allows services to be edited or deleted.

<h3 id="services_list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|A page number within the paginated result set.|

> Example responses

> 200 Response

```json
{
  "count": 0,
  "next": "http://example.com",
  "previous": "http://example.com",
  "results": [
    {
      "title": "string",
      "description": "string",
      "cluster": "http://example.com",
      "config": {},
      "labels": {},
      "annotations": {},
      "api_version": "string",
      "kind": "string",
      "port": -2147483648,
      "namespace": "string",
      "kuid": "string",
      "selector": {},
      "target_port": -2147483648
    }
  ]
}
```

<h3 id="services_list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="services_list-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» count|integer|true|none|none|
|» next|string(uri)\|null|false|none|none|
|» previous|string(uri)\|null|false|none|none|
|» results|[[KubernetesService](#schemakubernetesservice)]|true|none|none|
|»» title|string|true|none|none|
|»» description|string\|null|false|none|none|
|»» cluster|string(uri)\|null|false|none|none|
|»» config|object\|null|false|none|none|
|»» labels|object|false|none|none|
|»» annotations|object\|null|false|none|none|
|»» api_version|string|false|none|none|
|»» kind|string|true|none|none|
|»» port|integer|false|none|none|
|»» namespace|string|false|none|none|
|»» kuid|string\|null|false|none|Object's UID in the cluster|
|»» selector|object|false|none|none|
|»» target_port|integer|false|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_create

<a id="opIdservices_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/services/', params={

}, headers = headers)

print r.json()

```

`POST /services/`

API endpoint that allows services to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesService](#schemakubernetesservice)|true|none|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_read

<a id="opIdservices_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/services/{id}/', params={

}, headers = headers)

print r.json()

```

`GET /services/{id}/`

API endpoint that allows services to be edited or deleted.

<h3 id="services_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_update

<a id="opIdservices_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://127.0.0.1:8000/api/services/{id}/', params={

}, headers = headers)

print r.json()

```

`PUT /services/{id}/`

API endpoint that allows services to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesService](#schemakubernetesservice)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_partial_update

<a id="opIdservices_partial_update"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.patch('http://127.0.0.1:8000/api/services/{id}/', params={

}, headers = headers)

print r.json()

```

`PATCH /services/{id}/`

API endpoint that allows services to be edited or deleted.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_partial_update-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesService](#schemakubernetesservice)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_partial_update-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_delete

<a id="opIdservices_delete"></a>

> Code samples

```python
import requests

r = requests.delete('http://127.0.0.1:8000/api/services/{id}/', params={

)

print r.json()

```

`DELETE /services/{id}/`

API endpoint that allows services to be edited or deleted.

<h3 id="services_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

<h3 id="services_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_deploy_read

<a id="opIdservices_deploy_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/services/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`GET /services/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

<h3 id="services_deploy_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_deploy_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_deploy_create

<a id="opIdservices_deploy_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/services/{id}/deploy/', params={

}, headers = headers)

print r.json()

```

`POST /services/{id}/deploy/`

Action to deploy the kubernetes resource to target cluster.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_deploy_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesService](#schemakubernetesservice)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_deploy_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_k_delete_read

<a id="opIdservices_k_delete_read"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://127.0.0.1:8000/api/services/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`GET /services/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespace.

<h3 id="services_k_delete_read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 200 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_k_delete_read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

## services_k_delete_create

<a id="opIdservices_k_delete_create"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://127.0.0.1:8000/api/services/{id}/k_delete/', params={

}, headers = headers)

print r.json()

```

`POST /services/{id}/k_delete/`

Action to delete the kubernetes resource from the cluster/namespace.

> Body parameter

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_k_delete_create-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[KubernetesService](#schemakubernetesservice)|true|none|
|id|path|string(uuid)|true|A UUID string identifying this kubernetes service.|

> Example responses

> 201 Response

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}
```

<h3 id="services_k_delete_create-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|[KubernetesService](#schemakubernetesservice)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
Basic
</aside>

# Schemas

<h2 id="tocStargetcluster">TargetCluster</h2>

<a id="schematargetcluster"></a>

```json
{
  "title": "string",
  "api_endpoint": "http://example.com",
  "telemetry_endpoint": "http://example.com",
  "config": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|api_endpoint|string(uri)|true|none|Cluster Endpoint URL|
|telemetry_endpoint|string(uri)|true|none|Telemetry Endpoint URL|
|config|object\|null|false|none|Configuration data stored as an encrypted blob in the database|

<h2 id="tocSkubernetescontainer">KubernetesContainer</h2>

<a id="schemakubernetescontainer"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "image_name": "string",
  "image_tag": "string",
  "image_pull_policy": "Always",
  "command": "string",
  "args": "string",
  "port": -2147483648,
  "volume_mount": "http://example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|image_name|string|false|none|Properly qualified image name to execute this job within|
|image_tag|string|false|none|Tag name for the image to be used for this job|
|image_pull_policy|string|false|none|none|
|command|string\|null|false|none|Command to run when instantiating container|
|args|string\|null|false|none|Comma separated args to run with command when instantiating container.|
|port|integer|false|none|none|
|volume_mount|string(uri)\|null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|image_pull_policy|Always|
|image_pull_policy|IfNotPresent|
|image_pull_policy|Never|

<h2 id="tocSkubernetesdeployment">KubernetesDeployment</h2>

<a id="schemakubernetesdeployment"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "replicas": -2147483648,
  "pod_template": "http://example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|api_version|string|false|none|none|
|kind|string|true|none|none|
|port|integer|false|none|none|
|namespace|string|false|none|none|
|kuid|string\|null|false|none|Object's UID in the cluster|
|selector|object|false|none|none|
|replicas|integer|false|none|none|
|pod_template|string(uri)|true|none|none|

<h2 id="tocSkubernetesingress">KubernetesIngress</h2>

<a id="schemakubernetesingress"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "hostname": "string",
  "path": "string",
  "target_service": "http://example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|api_version|string|false|none|none|
|kind|string|true|none|none|
|port|integer|false|none|none|
|namespace|string|false|none|none|
|kuid|string\|null|false|none|Object's UID in the cluster|
|hostname|string|false|none|none|
|path|string|false|none|none|
|target_service|string(uri)|true|none|none|

<h2 id="tocSkubernetesjob">KubernetesJob</h2>

<a id="schemakubernetesjob"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "backoff_limit": -2147483648,
  "pod_template": "http://example.com"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|api_version|string|false|none|none|
|kind|string|true|none|none|
|port|integer|false|none|none|
|namespace|string|false|none|none|
|kuid|string\|null|false|none|Object's UID in the cluster|
|backoff_limit|integer|false|none|none|
|pod_template|string(uri)|true|none|none|

<h2 id="tocSkubernetesnamespace">KubernetesNamespace</h2>

<a id="schemakubernetesnamespace"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "exists": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|api_version|string|false|none|none|
|kind|string|true|none|none|
|exists|boolean|false|none|none|

<h2 id="tocSkubernetespodtemplate">KubernetesPodTemplate</h2>

<a id="schemakubernetespodtemplate"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "volume": "http://example.com",
  "primary_container": "http://example.com",
  "secondary_container": "http://example.com",
  "restart_policy": "Always"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|volume|string(uri)\|null|false|none|none|
|primary_container|string(uri)|true|none|none|
|secondary_container|string(uri)\|null|false|none|none|
|restart_policy|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|restart_policy|Always|
|restart_policy|OnFailure|
|restart_policy|Never|

<h2 id="tocSkubernetesservice">KubernetesService</h2>

<a id="schemakubernetesservice"></a>

```json
{
  "title": "string",
  "description": "string",
  "cluster": "http://example.com",
  "config": {},
  "labels": {},
  "annotations": {},
  "api_version": "string",
  "kind": "string",
  "port": -2147483648,
  "namespace": "string",
  "kuid": "string",
  "selector": {},
  "target_port": -2147483648
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|description|string\|null|false|none|none|
|cluster|string(uri)\|null|false|none|none|
|config|object\|null|false|none|none|
|labels|object|false|none|none|
|annotations|object\|null|false|none|none|
|api_version|string|false|none|none|
|kind|string|true|none|none|
|port|integer|false|none|none|
|namespace|string|false|none|none|
|kuid|string\|null|false|none|Object's UID in the cluster|
|selector|object|false|none|none|
|target_port|integer|false|none|none|

