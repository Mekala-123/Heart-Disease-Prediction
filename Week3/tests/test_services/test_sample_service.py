from app.services.sample_service import SampleService

def test_service_output():
    service = SampleService()
    result = service.get_sample(1)
    assert result["id"] == 1
