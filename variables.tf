# -----------------------------------------------------------------------------
# Variables: General
# -----------------------------------------------------------------------------

variable "environment" {
  description = "AWS resource environment/prefix"
  default     = "test"
}

variable "region" {
  description = "AWS region"
  default     = "ap-southeast-1"
}

variable "resource_tag_name" {
  description = "Resource tag name for cost tracking"
  default     = "test_tag"
}
